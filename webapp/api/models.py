from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    power = models.IntegerField()
    weight = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
