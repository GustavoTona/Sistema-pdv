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


     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
     preco = models.DecimalField(max_digits=10, decimal_places=2, default=0) 

def __str__(self):
        return f"{self.cliente} - {self.produto}"
