from django.db import models
from datetime import *


class Client(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    fecha_alta = models.DateField(datetime.now(), editable=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
