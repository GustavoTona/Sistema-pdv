from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include

from dashboard.views import dashboard

from vendas.views import VendaListView, VendaDeleteView, minha_view

from clientes.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, home

urlpatterns = [

    # path do app Produtos
    path('admin/', admin.site.urls),
    path("produtos", ProdutoListView.as_view(), name="produto_list"),
    path("create_produto", ProdutoCreateView.as_view(), name="produto_create"),
    path("update/<int:pk>", ProdutoUpdateView.as_view(), name="produto_update"),
    path("delete/<int:pk>", ProdutoDeleteView.as_view(), name="produto_delete"),

    path("", home, name="inicio"), #name cria uma rota para ser puxada, exemplo inicio

    # path do app Clientes
    path("clientes/", ClienteListView.as_view(), name="cliente_list"), 
    path("create_cliente", ClienteCreateView.as_view(), name="cliente_create"),
    path("update_cliente/<int:pk>", ClienteUpdateView.as_view(), name="cliente_update"),
    path("delete_cliente/<int:pk>", ClienteDeleteView.as_view(), name="cliente_delete"),
    
    # path do app Vendas    
    path("vendas", VendaListView.as_view(), name="venda_list"),
    path('vendas_create', minha_view, name='vendas_create'),
    path("delete_venda/<int:pk>", VendaDeleteView.as_view(), name="venda_delete"),


    # path do app Dashboard
    path('dashboard', dashboard, name='dashboard'),

     # path do app Usuarios
    path('auth/', include("usuarios.urls"))  



]

    # path("clientes/", include('clientes.url')) #include para chamar o app clientes, import include
