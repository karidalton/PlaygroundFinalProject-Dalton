from django.contrib import admin
from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_alta", "email")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_filter = ("nombre",)
    date_hierarchy = "fecha_alta"


admin.site.register(models.Client, ClientAdmin)
