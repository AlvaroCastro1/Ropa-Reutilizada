from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Cuenta

# clase (herencia)
def lista_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'lista_cuentas.html', {'cuentas': cuentas})

def home(request):
    return render(request, 'index.html')

def login(request):
      return render(request, 'InicioSesionCliente.html')

def registro(request):
      return render(request, 'RegistroCliente.html')