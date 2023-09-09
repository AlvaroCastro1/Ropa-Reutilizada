from django.db import models

# Create your models here.

# aqui vamos a crear las "tablas"

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    activo = models.IntegerField(null=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    anio_publicacion = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)