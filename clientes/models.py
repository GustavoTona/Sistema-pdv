from django.db import models

# Create your models here.

class Cliente(models.Model): #classe cliente, precisamos especificar o que tem dentro
    primeiro_nome = models.CharField(
        max_length=50, 
        null=False, 
        blank=False
        )
    sobrenome = models.CharField(
        max_length=50, 
        null=False, 
        blank=False
        )
    
    nascimento = models.CharField(
        max_length=8, 
        null=False, 
        blank=False
        )

    cpf = models.CharField(
        max_length=11, 
        null=False, 
        blank=False
        )
    
    telefone = models.CharField(
        max_length=9, 
        null=False, 
        blank=False
        )
    
    endereco = models.CharField(
        max_length=50, 
        null=False, 
        blank=False
        )

    registrado_em = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False
        )
    
    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenome}"