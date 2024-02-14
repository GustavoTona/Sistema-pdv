from django.shortcuts import render, HttpResponse
from clientes.models import Cliente
from vendas.models import Produto
from vendas.models import Venda
from django.db.models import Sum

def dashboard(request):
    # Obtenha a contagem de clientes
    total_clientes = Cliente.objects.count()

    # Obtenha o total de vendas e o valor total das vendas
    produto = Venda.objects.count()
    faturamento_vendas = Venda.objects.aggregate(Sum('preco'))['preco__sum']
    vendas = Venda.objects.all()
    # Passe os dados para o template
    context = {
        
        'total_clientes': total_clientes,
        'total_vendas': produto,
        'faturamento_vendas': faturamento_vendas,
        'vendas': vendas
    }

    # Renderize a página com o template e os dados

    return render(request, 'dashboard/dashboard_list.html', context)



 

