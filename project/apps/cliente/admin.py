from django.contrib import admin
from . import models

admin.site.site_title = "cliente"

class ClientAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha_alta", "email")
    list_display_links = ("nombre",)
    search_fields = ("nombre", "apellido")
    ordering = ("nombre",)
    list_filter = ("nombre",)
    date_hierarchy = "fecha_alta"


admin.site.register(models.Client, ClientAdmin)
