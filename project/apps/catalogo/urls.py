from django.urls import path
from .views import *

app_name = "catalogo"

urlpatterns = [
    path("", index, name="index"),
    path("categoria/list/", CategoriaList.as_view(), name="categoria_list"),
    path("categoria/form/", CategoriaCreate.as_view(), name="categoria_form"),
    path("categoria/update/<int:pk>/",
         CategoriaUpdate.as_view(), name="categoria_update"),
    path("categoria/delete/<int:pk>/",
         CategoriaDelete.as_view(), name="categoria_delete"),
    path("producto/list/", ProductoList.as_view(), name="producto_list"),
    path("producto/form/", ProductoCreate.as_view(), name="producto_form"),
    path("producto/update/<int:pk>/",
         ProductoUpdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>/", ProductoDelete.as_view(),
         name="producto_confirm_delete"),
    path("producto/detail/<int:pk>/",
         ProductoDetail.as_view(), name="producto_detail"),
    path("venta/list/", VentaList.as_view(), name="venta_list"),
    path("venta/form/", VentaCreate.as_view(), name="venta_form"),
    path("venta/update/<int:pk>/", VentaUpdate.as_view(), name="venta_update"),
    path("venta/delete/<int:pk>/", VentaDelete.as_view(),
         name="venta_confirm_delete"),
]
