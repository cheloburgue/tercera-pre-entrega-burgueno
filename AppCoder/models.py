from django.db import models

# Create your models here.

class Instrumento(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    codigo_instrumento = models.IntegerField()
    def __str__(self):
        return f"{self.tipo} - {self.marca} - {self.codigo_instrumento}"

class Precio(models.Model):
    codigo_instrumento = models.IntegerField()
    precio = models.FloatField()
    def __str__(self):
        return f"{self.codigo_instrumento} - {self.precio}"
    
class Locales(models.Model):
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.direccion} - {self.localidad}"