from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Venda
from django.views.generic import ListView, DeleteView

class VendaListView(ListView):
    model = Venda

class VendaDeleteView(DeleteView):
    model = Venda
    success_url = reverse_lazy("venda_list")

from .forms import ItemForm

def minha_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # Lógica para salvar os dados no banco de dados
            cliente = form.cleaned_data['cliente']
            produto = form.cleaned_data['produto']
            preco = form.cleaned_data['preco']
           
          # Crie uma instância de Venda associando o cliente e o produto
            venda = Venda.objects.create(cliente=cliente, produto=produto, preco=preco)

            # Redirecione ou faça qualquer outra ação necessária após salvar
            return redirect('venda_list')  # Substitua 'minha_view' pelo nome da sua view

    else:
        form = ItemForm()

    return render(request, 'vendas/venda_create.html', {'form': form})