from django.db import models

# Create your models here.

class Venda(models.Model):
    cliente = models.CharField(
        max_length=100
        )
    
    produto = models.CharField(
        max_length=100
        )
    preco = models.CharField(
        max_length=100
    )
    venda_em = models.DateField(
        null=True
    )

    def __str__(self):
        return f"{self.cliente} {self.produto} {self.preco}"