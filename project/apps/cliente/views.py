from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.


def index(request):
    return render(request, "cliente/index.html")


def cliente_list(request):
    client = models.Client.objects.all()
    context = {"clientes": client}

    return render(request, "cliente/cliente_list.html", context)


def cliente_create(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    else:  # if request.method == "GET":
        form = forms.ClientForm()
    return render(request, "cliente/cliente_create.html", {"form": form})
