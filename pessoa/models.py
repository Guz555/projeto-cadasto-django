from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    ativa = models.BooleanField(default=True)
    data_nascimento = models.DateField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nome_completo


class Contato(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
