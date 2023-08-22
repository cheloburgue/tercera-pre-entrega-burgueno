from django.db import models

# Create your models here.

class Instrumento(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    codigo_instrumento = models.IntegerField()

class Precio(models.Model):
    codigo_instrumento = models.IntegerField()
    precio = models.FloatField()

class Locales(models.Model):
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)