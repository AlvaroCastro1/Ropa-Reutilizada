from django.shortcuts import render
from django.views.generic.list import ListView

# clase (herencia)

def home(request):
    return render(request, 'index.html')

def login(request):
      return render(request, 'InicioSesionCliente.html')

def registro(request):
      return render(request, 'RegistroCliente.html')

def catalogo(request):
      return render(request, 'catalogo.html')