from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import VendaForm, Venda

     
def ClienteDados(request):
    form = VendaForm()

    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            # Obtenha os dados do formulário
            cliente = form.cleaned_data['cliente']
            produto = form.cleaned_data['produto']
        

            # Crie uma instância do modelo Venda e salve os dados
            venda = Venda(cliente=cliente, produto=produto)
            venda.save()

            return redirect('/vendas_sucesso')  # Substitua 'sucesso' pelo nome da sua página de sucesso

        return render(request, 'vendas/venda_form.html', {'form': form})




    
    
