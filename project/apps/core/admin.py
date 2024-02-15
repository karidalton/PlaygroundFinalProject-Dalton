from django.contrib import admin
from . import models

admin.site.site_title = "core"


class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "mensaje", "fecha_envio")
    list_display_links = ("mensaje",)
    search_fields = ("nombre", "email")
    ordering = ("fecha_envio",)
    list_filter = ("nombre",)
    date_hierarchy = "fecha_envio"


admin.site.register(models.Contacto, ContactoAdmin)
