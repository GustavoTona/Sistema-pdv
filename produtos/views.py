from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView           
from .models import Produto

class ProdutoListView(ListView):
       model = Produto

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["name", "preco", "quantidade"]
    success_url = reverse_lazy("produto_list")

class ProdutoUpdateView(UpdateView):
       model = Produto
       fields = ["name", "preco", "quantidade"]
       success_url = reverse_lazy("produto_list")

class ProdutoDeleteView(DeleteView): 
      model = Produto
      success_url = reverse_lazy("produto_list")


from django.http import HttpResponse
from django.shortcuts import render

def home(request):
      return render(request, "index.html")