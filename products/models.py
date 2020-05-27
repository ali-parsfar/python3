from django.db import models
from django.utils import timezone

# Create your models here.


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    discount = models.FloatField()


class Base(models.Model):
    name = models.CharField(max_length=12)
    ingrediants = models.CharField(max_length=255)


class Cakes(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    size = models.CharField(max_length=255)
    toping = models.CharField(max_length=255)
    weight = models.FloatField()
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2083, default="defult.jpg")
