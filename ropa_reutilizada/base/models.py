from django.db import models

# Create your models here.

# aqui vamos a crear las "tablas"

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    activo = models.IntegerField(null=True)