from django.contrib import admin
from .models import *

admin.site.site_title = "Catalogo"

admin.site.register(Categoria)
# admin.site.register(models.ClasificacionContenido)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria_id", "nombre", "fecha_creacion")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria_id", "nombre")
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_creacion"

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)
