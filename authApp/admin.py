from django.contrib import admin
from .models.person import Persona
from .models.clientes import Cliente
from .models.purchase import Compra

# Register your models here.

admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Compra)