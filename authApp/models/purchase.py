from django.db import models

from authApp.models.clientes import Cliente
from .clientes import Cliente
class Compra(models.Model):
    total_count = models.PositiveIntegerField()
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
