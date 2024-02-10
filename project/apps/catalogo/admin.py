from django.contrib import admin
from .models import *

admin.site.site_title = "Catalogo"

admin.site.register(Categoria)
# admin.site.register(models.ClasificacionContenido)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria_id", "nombre", "precio", "fecha_creacion")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_creacion"


class VentaAdmin(admin.ModelAdmin):
    list_display = ("operacion", "fecha_operacion",
                    "articulo","cantidad", "precio_unitario", "precio_neto")
    list_display_links = ("operacion",)
    search_fields = ("operacion", "cliente", "fecha_operacion", "articulo")
    ordering = ("operacion", "fecha_operacion")
    list_filter = ("operacion",)
    date_hierarchy = "fecha_operacion"


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
