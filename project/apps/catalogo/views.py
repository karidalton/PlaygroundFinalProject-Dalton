from django.shortcuts import render, redirect
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


def index(request):
    return render(request, "catalogo/index.html")


class CategoriaList(ListView):
    model = Categoria
    template_name = 'catalogo/categoria_list.html'

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = Categoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = Categoria.objects.all()
        return object_list


class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("catalogo:categoria_list")


class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("catalogo:categoria_list")


class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy("catalogo:categoria_list")


class ProductoList(ListView):
    model = Producto
    template_name = 'catalogo/producto_list.html'

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = Producto.objects.all()
        return object_list


class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("catalogo:producto_list")


class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("catalogo:producto_list")


class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("catalogo:producto_list")


class ProductoDetail(DetailView):
    model = Producto


class VentaList(ListView):
    model = Venta
    template_name = 'catalogo/venta_list.html'

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = Venta.objects.filter(operacion__icontains=consulta)
        else:
            object_list = Venta.objects.all()
        return object_list


class VentaCreate(LoginRequiredMixin, CreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy("catalogo:venta_list")


class VentaUpdate(LoginRequiredMixin, UpdateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy("catalogo:venta_list")


class VentaDelete(LoginRequiredMixin, DeleteView):
    model = Venta
    success_url = reverse_lazy("catalogo:venta_list")
