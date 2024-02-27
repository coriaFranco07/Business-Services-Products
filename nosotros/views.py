from django.shortcuts import render
from .models import Nosotros, Ubicacion

# Create your views here.

def nosotros(request):
    nosotros = Nosotros.objects.all()
    sucursales= Ubicacion.objects.all()
    return render(request, "nosotros/nosotros.html", {"nosotros":nosotros, "sucursales":sucursales})


