from django.contrib import admin
from .models import  ImagenProducto, BaseCliente, BaseDonacion, BaseCDonante, BaseIDProducto, BaseApartado, BaseAProducto, BaseCanjeo


class ImagenProductoInline(admin.TabularInline):  # Opciones: admin.StackedInline o admin.TabularInline
    model = ImagenProducto
    extra = 1  # Puedes ajustar este valor según la cantidad deseada de imágenes para un producto

class IProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]

class BaseIDProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProducto]

admin.site.register(BaseIDProducto, BaseIDProductoAdmin)  # Registrar el modelo BaseIDProducto con el administrador

admin.site.register(BaseCliente)
admin.site.register(BaseDonacion)
admin.site.register(BaseCDonante)
admin.site.register(BaseApartado)
admin.site.register(BaseAProducto)
admin.site.register(BaseCanjeo)
