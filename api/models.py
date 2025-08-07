from django.db import models

class Autor (models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    data_nasc = models.DateField(null=False, blank=False)
    nacionalidade = models.CharField(max_length=50, null=False, blank=False)
    biografia = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
