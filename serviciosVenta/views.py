from django.shortcuts import render
from . import models

# Create your views here.

def venta(request):
    autos = models.Auto.objects.all()
    return render(request, 'venta.html', {"autos":autos})

def servicios(request):
    servicios = models.Servicio.objects.all()
    return render(request, 'servicios.html', {"servicios":servicios})