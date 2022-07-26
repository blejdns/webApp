from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    sale = models.BooleanField()
    sale_price = models.IntegerField(null=True)
    sale_date_expired = models.DateField(null=True)
