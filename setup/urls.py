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
from django.contrib import admin
from django.urls import path
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("produtos", ProdutoListView.as_view(), name="produto_list"),
    path("create", ProdutoCreateView.as_view(), name="produto_create"),
    path("update/<int:pk>", ProdutoUpdateView.as_view(), name="produto_update"),
    path("delete/<int:pk>", ProdutoDeleteView.as_view(), name="produto_delete"),
    path("", home),
]