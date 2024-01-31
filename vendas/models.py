from django.db import models

class Venda(models.Model):
     
     primeiro_nome = models.CharField( 
          max_length=50
          )
     sobrenome = models.CharField( 
          max_length=50
          )
     nome_produto = models.CharField( 
          max_length=50
          )
     preco = models.CharField( 
          max_length=50
          )