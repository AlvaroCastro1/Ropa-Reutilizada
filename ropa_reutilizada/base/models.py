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
        
class BaseCliente(models.Model):
    IDCliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    ApellidoM = models.CharField(max_length=30)
    ApellidoP = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    Contrasena = models.CharField(max_length=30)
    Monedero = models.DecimalField(max_digits=4, decimal_places=2)

class BaseDonacion(models.Model):
    IDDonacion = models.AutoField(primary_key=True)
    FechaDeDonacion = models.DateTimeField()

class BaseCDonante(models.Model):
    IDDonante = models.AutoField(primary_key=True)
    IDCliente1 = models.ForeignKey(BaseCliente, on_delete=models.CASCADE)
    IDDonacion1 = models.ForeignKey(BaseDonacion, on_delete=models.CASCADE)
    PuntosAgregados = models.DecimalField(max_digits=10, decimal_places=2)

class BaseApartado(models.Model):
    IDApartado = models.AutoField(primary_key=True)
    FHDeApartado = models.DateTimeField()
    ProductosT = models.IntegerField()
    CantidadT = models.DecimalField(max_digits=4, decimal_places=2)

class BaseAProducto(models.Model):
    IDAProducto = models.AutoField(primary_key=True)
    IDIProducto1 = models.ForeignKey(IProducto, on_delete=models.CASCADE)
    IDApartado1 = models.ForeignKey(BaseApartado, on_delete=models.CASCADE)
    IDCliente2 = models.ForeignKey(BaseCliente, on_delete=models.CASCADE)

class BaseCanjeo(models.Model):
    IDCanjeo = models.AutoField(primary_key=True)
    IDIProducto2 = models.ForeignKey(IProducto, on_delete=models.CASCADE)
    IDCliente3 = models.ForeignKey(BaseCliente, on_delete=models.CASCADE)
    FHCanjeo = models.DateTimeField()

