from django.db import models
from inventarioApp.models.client import Client

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    name_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    totalValue = models.PositiveBigIntegerField()
    purchaseDate = models.DateField()
    product = models.CharField(max_length=100)
