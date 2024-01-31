
from .models import Venda
from django.views.generic import ListView


class VendaForm(ListView):
    model = Venda
