from django.http import HttpResponse
from django.shortcuts import render, redirect # para redicionar a pagina quand ologar 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django #para mudar o login que está conflitanto com a def
from produtos.views import home # puxando a pagina inicio
from django.contrib.auth.decorators import login_required #puxar na def para ver apenas logado
# Create your views here.

def cadastro (request): 
    if request.method == "GET":
        return render (request, "usuarios/cadastro.html")
    else: #senao 
        username = request.POST.get("usuario") 
        first_name = request.POST.get("primeironome")
        last_name = request.POST.get("sobrenome")
        email = request.POST.get("email")
        password = request.POST.get("senha")
        
        user = User.objects.filter(username=username).first() #conferir se ja existe o usuari 
        if user:
            return HttpResponse("Já existe um usuario com esse username") # se existe mostrar a mensagem
     
        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, email=email, password=password
            )
        user.save()
        return HttpResponse("Cadastrado com sucesso!")

def login(request):

    if request.method == "GET":
        return render (request, 'usuarios/login.html')
    else: #se nao 
        username = request.POST.get("usuario") 
        password = request.POST.get("senha")

        user = authenticate(username=username, password=password)

        if user: 
            login_django(request, user)

            return redirect("inicio")
        else:
            return HttpResponse("Email ou senha invalidos")