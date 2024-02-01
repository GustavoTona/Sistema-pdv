from django.shortcuts import render
from .models import Venda
from django.views.generic import ListView

class VendaListView(ListView):
    model = Venda


from .forms import ItemForm

def minha_view(request):
    form = ItemForm()
    return render(request, 'vendas/venda_create.html', {'form': form})