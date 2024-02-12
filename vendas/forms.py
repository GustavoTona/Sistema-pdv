from django import forms
from clientes.models import Cliente
from produtos.models import Produto

class ItemForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())
    preco = forms.DecimalField(max_digits=10, decimal_places=2, disabled=False)  # Adicione um campo para exibir o preço do produto
    salvar = forms.BooleanField(widget=forms.HiddenInput(), required=False)

