from django import forms 

class InstrumentoForm(forms.Form):
    tipo = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
    codigo_instrumento = forms.IntegerField()

class PreciosForm(forms.Form):
    codigo_instrumento = forms.IntegerField()
    precio = forms.FloatField()

class LocalesForm(forms.Form):
    direccion = forms.CharField(max_length=100)
    localidad = forms.CharField(max_length=100)