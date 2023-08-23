from django.shortcuts import render
from django.http import HttpResponse
from .models import  Instrumento, Precio, Locales
from .forms import InstrumentoForm, PreciosForm, LocalesForm

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def instrumentos(request):
    if request.method == "POST":
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            tipo = info["tipo"]
            marca = info["marca"]
            codigo_instrumento = info["codigo_instrumento"]
            instrumento = Instrumento(tipo=tipo,marca=marca,codigo_instrumento=codigo_instrumento)
            instrumento.save()
            formulario_instrumento = InstrumentoForm()
            return render(request, "AppCoder/instrumentos.html", {"mensaje": "Instrumento creado!","formulario":formulario_instrumento})
        return render(request, "AppCoder/instrumentos.html", {"mensaje": "Datos Invalidos!"})
    else:
        formulario_instrumento = InstrumentoForm()
    return render(request, "AppCoder/instrumentos.html", {"formulario":formulario_instrumento})



def precios(request):
    if request.method == "POST":
        form = PreciosForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            codigo_instrumento = info["codigo_instrumento"]
            precio = info["precio"]
            precio = Precio(codigo_instrumento=codigo_instrumento,precio=precio)
            precio.save()
            formulario_precio = PreciosForm()
            return render(request, "AppCoder/precios.html", {"mensaje": "Precio Agregado!","formulario":formulario_precio})
        return render(request, "AppCoder/precios.html", {"mensaje": "Datos Invalidos!"})
    else:
        formulario_precio = PreciosForm()
    return render(request, "AppCoder/precios.html",{"formulario":formulario_precio})

def locales(request):
    if request.method == "POST":
        form = LocalesForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            direccion = info["direccion"]
            localidad = info["localidad"]
            local = Locales(direccion=direccion, localidad=localidad)
            local.save()
            formulario_locales = PreciosForm()
            return render(request, "AppCoder/locales.html", {"mensaje": "Local Agregado!","formulario": formulario_locales})
        return render(request, "AppCoder/locales.html", {"mensaje": "Datos Invalidos!"})
    else:
        formulario_locales = LocalesForm()
    return render(request, "AppCoder/locales.html",{"formulario":formulario_locales})


def buscarInstrumento(request):
    return render(request, "AppCoder/buscarInstrumento.html")

def buscarDatos(request):
    marca = request.GET["marca"]
    if marca != "" :
        instrumento = Instrumento.objects.filter(marca__icontains=marca)
        if instrumento:
            return render(request, "AppCoder/resultadoBusqueda.html",{"instrumentos":instrumento})
        else:
            return render(request, "AppCoder/buscarInstrumento.html",{"mensaje":"No se encontraron resultados para la busqueda!"})
    else:
        return render(request, "AppCoder/buscarInstrumento.html",{"mensaje":"No se ingresaron datos!"})