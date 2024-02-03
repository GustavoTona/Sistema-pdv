from django.views.generic import ListView, CreateView, UpdateView, DeleteView #importar o list 

from django.urls import reverse_lazy #puxar para quando concluir o create voltar para a pagina list automatico
from .models import Cliente
# Create your views here.

#Essa funcão de cima mudou poara essa de baixo, essa de baixo é mais moderna

class ClienteListView(ListView):
    model = Cliente #Por padrão a list view procura um template, mesmo nome app e _list 

class ClienteCreateView(CreateView): #quando usar o Createview precisa setar o modelo fields
    model = Cliente
    fields = ["primeiro_nome", "sobrenome", "nascimento", "cpf", "telefone", "endereco"] 
    success_url = reverse_lazy ("cliente_list")

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ["primeiro_nome", "sobrenome", "nascimento", "cpf", "telefone", "endereco"] 
    success_url = reverse_lazy ("cliente_list")

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy ("cliente_list") #retornar ao inicio 
