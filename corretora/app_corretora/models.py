from django.db import models

class Cliente(models.Model):
    cpf_cliente = models.CharField(primary_key=True, max_length=11)
    nome_cliente = models.CharField(max_length=200)

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    liquidez = models.CharField(max_length=200)

class ProdutosDoCliente(models.Model):
    cpf_cliente = models.CharField(max_length=11)
    nome_cliente = models.CharField(max_length=200)
    nome_produto = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    liquidez = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome_cliente} - {self.nome_produto}"
