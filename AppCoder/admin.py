from django.contrib import admin
from .models import Instrumento, Precio, Locales

# Register your models here.
admin.site.register(Instrumento)
admin.site.register(Precio)
admin.site.register(Locales)