from django.urls import path
from . import views


urlpatterns = [
    path('lista_cuentas/', views.lista_cuentas, name='lista_cuentas'),
]
