from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = Cliente.objects.filter(nombre__icontains=consulta)
        else:
            object_list = Cliente.objects.all()
        return object_list


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")


class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente:cliente_list")


class ClienteDetail(DetailView):
    model = Cliente
