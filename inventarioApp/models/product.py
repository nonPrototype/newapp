from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productExpiration = models.DateTimeField()
    productDescription = models.CharField(max_length=500)