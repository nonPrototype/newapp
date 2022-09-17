from mailbox import NoSuchMailboxError
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return self.nombre