# seu_app/forms.py

from django import forms
from clientes.models import Cliente
from produtos.models import Produto


class ClienteFormulario(forms.Form):
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



from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ClienteFormulario

     
def ClienteDados(request):
    form = ClienteFormulario()

    if request.method == 'POST':
        form = ClienteFormulario(request.POST)
        if form.is_valid():
            # Obtenha os dados do formulário
            cliente = form.cleaned_data['cliente']
            produto = form.cleaned_data['produto']
        

            # Crie uma instância do modelo Venda e salve os dados
            venda = Venda(cliente=cliente, produto=produto)
            venda.save()

            return redirect('/vendas_sucesso')  # Substitua 'sucesso' pelo nome da sua página de sucesso

        return render(request, 'vendas/venda_form.html', {'form': form})




    
    
