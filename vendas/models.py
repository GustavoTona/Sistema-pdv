from django.db import models
from django import forms
from clientes.models import Cliente
from produtos.models import Produto


class VendaForm(forms.Form):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), 
        empty_label=None
    )

    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(), 
        empty_label=None
        
    )

    preco = forms.ModelChoiceField(
        queryset=Produto.objects.all(), 
        empty_label=None
    )

    def __str__(self):
        return f'{self.cliente} - {self.produto} {self.preco}'
    
from django.db import models

class Venda(models.Model):
    cliente = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
    venda_em = models.CharField(max_length=100)
    # Outros campos do seu modelo, se houver

    def __str__(self):
        return f'{self.cliente} - {self.produto}'