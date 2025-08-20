from django.db import models

class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=18)
    telefone = models.CharField(max_length=20)

class Categoria(models.Model):
    nome  = models.CharField(max_length=50, unique = True)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null = True, blank = True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null = True)
    #Se apagar a categoria, o prod continua existindo

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    localizacao = models.CharField(max_length=30)


#class User(models.Model):


#class Permission(models.Model):


