from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
