from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField(
        verbose_name="Produto",
        max_length=50, #quantia max de caracter
        null=False, #nao pode valores nulos 
        blank= False, #nao pode deixar o espço em branco
      
        )
    
    created_at = models.DateTimeField(
         verbose_name="Data de registro",
         auto_now_add=True, #registrar automatico a hora que foi adicionad o
         null=False,
         blank=False,
      )
    
    quantidade = models.CharField(
        verbose_name="Quantidade",
        max_length=5, #quantia max de caracter
        null=True, #nao pode valores nulos 
        blank= True, #nao pode deixar o espço em branco
    )

    preco = models.CharField(
        verbose_name="Preço",
        max_length=50, #quantia max de caracter
        null=False, #nao pode valores nulos 
        blank= False, #nao pode deixar o espço em branco
    )