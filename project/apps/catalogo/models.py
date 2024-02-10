from django.db import models
from django.utils import timezone
from cliente.models import Cliente


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    precio = models.FloatField()
    fecha_creacion = models.DateField(
        default=timezone.now, editable=False, verbose_name="fecha de creación")
    descripcion = models.TextField(
        null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return f"{self.nombre}, {self.precio}, {self.categoria}"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"


class Venta(models.Model):
    operacion = models.AutoField(primary_key=True)
    articulo = models.ForeignKey(
        Producto, null=True, blank=True, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    cantidad = models.FloatField()
    precio_unitario = models.FloatField(default=0, editable=True)
    precio_neto = models.FloatField(default=0, editable=True)
    fecha_operacion = models.DateField(
        default=timezone.now, editable=False, verbose_name="fecha de operación")

    def __str__(self):
        return f"{self.operacion}, {self.fecha_operacion}, {self.articulo}, {self.cantidad}, {self.precio_unitario}, {self.precio_neto}"
