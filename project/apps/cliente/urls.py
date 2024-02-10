from django.urls import path
from .views import *

app_name = "cliente"

urlpatterns = [
    #    path("", index, name="index"),
    path("cliente/list/", ClienteList.as_view(), name="cliente_list"),
    path("cliente/form/", ClienteCreate.as_view(), name="cliente_form"),
    path("cliente/update/<int:pk>/", ClienteUpdate.as_view(), name="cliente_update"),
    path("cliente/delete/<int:pk>/", ClienteDelete.as_view(),
         name="cliente_confirm_delete"),
    path("cliente/detail/<int:pk>/", ClienteDetail.as_view(), name="cliente_detail"),
]
