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

# Create your views here.


#def index(request):
#    return render(request, "cliente/index.html")


#def cliente_list(request):
#    client = models.Client.objects.all()
#    context = {"clientes": client}
#
#    return render(request, "cliente/cliente_list.html", context)


#def cliente_create(request) -> HttpResponse:
#    if request.method == "POST":
#        form = forms.ClientForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("cliente:cliente_list")
#    else:  # if request.method == "GET":
#        form = forms.ClientForm()
#    return render(request, "cliente/cliente_create.html", {"form": form})



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
    success_url = reverse_lazy("catalogo:venta_list")


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("catalogo:venta_list")


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("catalogo:venta_list")


class ClientDetail(DetailView):
    model = Client
