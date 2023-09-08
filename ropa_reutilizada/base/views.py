from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lista_clientes(pedido):
    return HttpResponse('Lista de Clientes')