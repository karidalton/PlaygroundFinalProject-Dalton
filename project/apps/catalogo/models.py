from django.db import models
from django.utils import timezone
from cliente.models import Client


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    categoria_id = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=150)
    precio = models.FloatField()
    fecha_creacion = models.DateField(
        default=timezone.now, editable=False, verbose_name="fecha de creación")

    descripcion = models.TextField(
        null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return f"{self.nombre}, {self.precio}, {self.categoria_id}"
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"


class Venta(models.Model):
    articulo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL, editable=False)
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    precio_neto = models.FloatField(editable=False)
    fecha_operacion = models.DateField(
        default=timezone.now, editable=False, verbose_name="fecha de operación")
    
    def save(self):
        self.precio_neto = float(self.precio_unitario * self.cantidad)

    def __str__(self):
        return f"{self.fecha_operacion}, {self.articulo}, {self.cantidad}, {self.precio_unitario}, {self.precio_neto}"
