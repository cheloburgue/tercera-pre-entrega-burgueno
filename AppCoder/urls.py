from django.urls import path
from .views import *

urlpatterns =[
    path("",inicio, name="inicio"), #Cuando no tiene nada en la url caiga inicio
    path("instrumentos/",instrumentos, name="instrumentos"),
    path("precios/",precios, name="precios"),   
    path("locales/",locales, name="locales"), # name es para poder invocarlo desde el href en el html y redireccionar botones a distintas paginas
    path("buscarInstrumento/", buscarInstrumento, name="buscarInstrumento"),
    path("buscarDatos/", buscarDatos, name="buscarDatos"),
]