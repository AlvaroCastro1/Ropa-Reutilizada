from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login, name='Inicia Sesion'),
    path('registrate/', views.registro, name='Crea Tu Cuenta')
]
