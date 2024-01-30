
from .models import Venda
from django.views.generic import ListView


class VendaListView(ListView):
    model = Venda
