from django.contrib import admin
from .models import IProducto, ImagenProducto

class ImagenProductoInline(admin.TabularInline):  # Opciones: admin.StackedInline o admin.TabularInline
    model = ImagenProducto
    extra = 1  # Puedes ajustar este valor según la cantidad deseada de imágenes para un producto

class IProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]

admin.site.register(IProducto, IProductoAdmin)