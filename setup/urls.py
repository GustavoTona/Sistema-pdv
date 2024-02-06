"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include

from dashboard.views import dashboard

from vendas.views import VendaListView, VendaDeleteView, minha_view

from clientes.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("produtos", ProdutoListView.as_view(), name="produto_list"),
    path("create_produto", ProdutoCreateView.as_view(), name="produto_create"),
    path("update/<int:pk>", ProdutoUpdateView.as_view(), name="produto_update"),
    path("delete/<int:pk>", ProdutoDeleteView.as_view(), name="produto_delete"),

    path("", home, name="inicio"), #name cria uma rota para ser puxada, exemplo inicio

    path("clientes/", ClienteListView.as_view(), name="cliente_list"), 
    path("create_cliente", ClienteCreateView.as_view(), name="cliente_create"),
    path("update_cliente/<int:pk>", ClienteUpdateView.as_view(), name="cliente_update"),
    path("delete_cliente/<int:pk>", ClienteDeleteView.as_view(), name="cliente_delete"),
    
    path("vendas", VendaListView.as_view(), name="venda_list"),
    path('vendas_create', minha_view, name='vendas_create'),
    path("delete_venda/<int:pk>", VendaDeleteView.as_view(), name="venda_delete"),

    path('dashboard', dashboard, name='dashboard')

]

    # path("clientes/", include('clientes.url')) #include para chamar o app clientes, import include
