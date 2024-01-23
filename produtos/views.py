from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Produto

class ProdutoListView(ListView):
       model = Produto

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["name", "preco"]
    success_url = reverse_lazy("produto_list")

class ProdutoUpdateView(UpdateView):
       model = Produto
       fields = ["name", "preco"]
       success_url = reverse_lazy("produto_list")