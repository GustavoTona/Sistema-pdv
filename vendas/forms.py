from django import forms
from clientes.models import Cliente
from produtos.models import Produto

class ItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Cliente.objects.all())
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())
    preco = forms.IntegerField()
    salvar = forms.BooleanField(widget=forms.HiddenInput(), required=False)