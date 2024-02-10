from django.urls import path
from .views import *

app_name = "cliente"

urlpatterns = [
    #    path("", index, name="index"),
    path("cliente/list/", ClientList.as_view(), name="cliente_list"),
    path("cliente/form/", ClientCreate.as_view(), name="cliente_form"),
    path("cliente/update/<int:pk>/", ClientUpdate.as_view(), name="cliente_update"),
    path("cliente/delete/<int:pk>/", ClientDelete.as_view(),
         name="cliente_confirm_delete"),
    path("cliente/detail/<int:pk>/", ClientDetail.as_view(), name="cliente_detail"),
]
