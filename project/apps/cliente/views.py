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


class ClientList(ListView):
    model = Client
    template_name = 'cliente/cliente_list.html'

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = Client.objects.filter(nombre__icontains=consulta)
        else:
            object_list = Client.objects.all()
        return object_list


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("cliente:cliente_list")


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("cliente:cliente_list")


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("cliente:cliente_list")


class ClientDetail(DetailView):
    model = Client
