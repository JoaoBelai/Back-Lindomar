from django.db import models

class Autor (models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nasc = models.DateField()
    nacionalidade = models.CharField(max_length=50)
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Editora(models.Model):
    editora = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.editora}"

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=255)
    descricao = models.TextField()
    idioma = models.CharField(max_length=255, default="Português")
    ano_publicacao = models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField(max_length=255, null=True, blank=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}: {self.subtitulo}"
