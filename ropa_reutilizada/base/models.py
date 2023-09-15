from django.db import models

# Create your models here.

# aqui vamos a crear las "tablas"

class IProducto(models.Model):
    IDIProducto = models.AutoField(primary_key=True)
    Talla = models.CharField(max_length=20)
    Color = models.CharField(max_length=15)
    Genero = models.CharField(max_length=20)
    Material = models.CharField(max_length=30)
    Tipo = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    PuntosC = models.DecimalField(max_digits=10, decimal_places=2)
    Destino = models.CharField(max_length=30)

    class Meta:
        db_table = 'iproductos'  # Especifica el nombre de la tabla en la base de datos
        # Nombres
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.IDIProducto} - {self.Descripcion}'

class ImagenProducto(models.Model):
    IDIProducto = models.ForeignKey(IProducto, on_delete=models.CASCADE)
    URLImagen = models.ImageField(upload_to="productos",null=True)

    class Meta:
        db_table = 'ImagenesProductos'  # Especifica el nombre de la tabla en la base de datos
        # Nombres
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
