import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro, Autor, Editora

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f"Iniciando o processamento do arquivo: {options['arquivo']}"))

        df = pd.read_csv(options["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options['truncate']:
            self.stdout.write(self.style.WARNING("Limpando a tabela de Livros..."))
            Livro.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Tabela de Livros limpa."))

        df['titulo'] = df['titulo'].fillna('').astype(str).str.strip()
        df['subtitulo'] = df['subtitulo'].fillna('').astype(str).str.strip()
        df['isbn'] = df['isbn'].fillna('').astype(str).str.strip()
        df['descricao'] = df['descricao'].fillna('').astype(str).str.strip()
        df['idioma'] = df['idioma'].fillna('Português').astype(str).str.strip()
        df['dimensoes'] = df['dimensoes'].fillna('').astype(str).str.strip()
        df['autor'] = pd.to_numeric(df['autor'], errors='coerce').astype('Int64')
        df['editora'] = pd.to_numeric(df['editora'], errors='coerce').astype('Int64')
        df['ano_publicacao'] = pd.to_numeric(df['ano_publicacao'], errors='coerce').astype('Int64')
        df['paginas'] = pd.to_numeric(df['paginas'], errors='coerce').astype('Int64')
        df['estoque'] = pd.to_numeric(df['estoque'], errors='coerce').astype('Int64')
        df['preco'] = pd.to_numeric(df['preco'], errors='coerce')
        df['desconto'] = pd.to_numeric(df['desconto'], errors='coerce')
        df['peso'] = pd.to_numeric(df['peso'], errors='coerce')
        df['disponivel'] = df['disponivel'].astype(bool)

        df.dropna(subset=['titulo', 'autor', 'editora', 'isbn'], inplace=True)
        df = df.query("titulo != '' and isbn != ''")

        if options["update"]:
            self.stdout.write(self.style.WARNING("O modo --update ainda precisa ser revisado, focando no modo de criação em massa."))

        else:
            objs_para_criar = []
            livros_pulados_por_id = 0
            
            self.stdout.write("Iniciando a preparação dos livros para criação...")
            for r in df.itertuples(index=False):
                try:
                    autor_obj = Autor.objects.get(id=r.autor)
                    editora_obj = Editora.objects.get(id=r.editora)

                    livro = Livro(
                        titulo=r.titulo,
                        subtitulo=r.subtitulo,
                        autor=autor_obj,
                        editora=editora_obj,
                        isbn=r.isbn,
                        descricao=r.descricao,
                        idioma=r.idioma,
                        ano_publicacao=r.ano_publicacao,
                        paginas=r.paginas,
                        preco=r.preco,
                        estoque=r.estoque,
                        desconto=r.desconto,
                        disponivel=r.disponivel,
                        dimensoes=r.dimensoes,
                        peso=r.peso
                    )
                    objs_para_criar.append(livro)
                    self.stdout.write(f"  [OK] Preparado para criar: {r.titulo}")

                except (Autor.DoesNotExist, Editora.DoesNotExist) as e:
                    self.stdout.write(self.style.ERROR(f"  [PULANDO] Livro '{r.titulo}' (ISBN: {r.isbn}) porque o ID de Autor/Editora não foi encontrado. Detalhe: {e}"))
                    livros_pulados_por_id += 1
                    continue
            
            self.stdout.write("-" * 30)
            self.stdout.write(f"Preparação concluída. Total de livros na lista para criação: {len(objs_para_criar)}")
            self.stdout.write(f"Total de livros pulados por ID inválido: {livros_pulados_por_id}")
            
            if objs_para_criar:
                self.stdout.write("Iniciando 'bulk_create'...")
                Livro.objects.bulk_create(objs_para_criar, ignore_conflicts=True)
                self.stdout.write(self.style.SUCCESS(f"Operação 'bulk_create' concluída. {len(objs_para_criar)} livros foram enviados para o banco (conflitos de ISBN foram ignorados)."))
            else:
                self.stdout.write(self.style.WARNING("Nenhum livro novo para adicionar."))