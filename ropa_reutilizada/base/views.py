from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Cuenta

# clase (herencia)
def lista_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'lista_cuentas.html', {'cuentas': cuentas})