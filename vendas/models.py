from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
     
     cliente = models.CharField( 
          max_length=50
          )
     produto = models.CharField( 
          max_length=50
          )
     
     preco = models.IntegerField(
          max_length=50 
          )  # Adicionando um campo para armazenar o preço

     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


