import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        df = pd.read_csv(options["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options['truncate']: Livro.objects.all().delete()

        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["autor"] = df["autor"].astype(int)
        df["editora"] = df["editora"].astype(int)
        df["isbn"] = df["isbn"].astype(str).str.strip()
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_publicacao"] = df["ano_publicacao"].astype(int)
        df["paginas"] = df["paginas"].astype(int)
        df["preco"] = df["preco"].astype(float)
        df["estoque"] = df["estoque"].astype(int)
        df["desconto"] = df["desconto"].astype(float)
        df["disponivel"] = df["disponivel"].astype(bool)
        df["dimensoes"] = df["dimensoes"].astype(str).str.strip()
        df["peso"] = df["peso"].astype(float)

        df = df.query("titulo != '' and subtitulo != '' ")

        if options["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Livro.objects.update_or_create(
                    titulo=r.titulo, subtitulo=r.subtitulo, autor=r.autor, editora=r.editora, isbn=r.isbn,
                    descricao=r.descricao, idioma=r.idioma, ano_publicacao=r.ano_publicacao, paginas=r.paginas,
                    preco=r.preco, estoque=r.estoque, desconto=r.desconto, disponivel=r.disponivel,
                    dimensoes=r.dimensoes, peso=r.peso
                )

                criados += int(created)
                atualizados += int(not atualizados)
            self.stdout.write(self.style.SUCCESS(f'Criados: {criados} | Atualizados: {atualizados}'))
        else:
            objs = [Livro(
                titulo=r.titulo, subtitulo=r.subtitulo, autor=r.autor, editora=r.editora, isbn=r.isbn,
                descricao=r.descricao, idioma=r.idioma, ano_publicacao=r.ano_publicacao, paginas=r.paginas,
                preco=r.preco, estoque=r.estoque, desconto=r.desconto, disponivel=r.disponivel,
                dimensoes=r.dimensoes, peso=r.peso
            ) for r in df.itertuples(index=False)]

            Livro.objects.bulk_create(objs, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f'Criados: {len(objs)}'))
            

