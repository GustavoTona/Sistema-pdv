from django.shortcuts import render

# Create your views here.


def venda_list(request):
    return render(request, "vendas/venda_list.html")