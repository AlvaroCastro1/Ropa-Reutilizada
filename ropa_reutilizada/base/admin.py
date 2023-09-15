from django.contrib import admin
from .models import IProducto, ImagenProducto

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1  # cantidad de imágenes para un producto

class IProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]

admin.site.register(IProducto, IProductoAdmin)
