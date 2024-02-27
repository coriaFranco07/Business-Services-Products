from django.shortcuts import render
from empleados.models import Empleado, CategoriaEmpleado

# Create your views here.
def empleado(request):
     empleados = Empleado.objects.all()
     return render(request, "empleados/empleados.html", {"empleados":empleados})


""" def categoria(request, categoria_id):
    categoria = CategoriaEmpleado.objects.get(id = categoria_id)
    empleados = Empleado.objects.filter(categorias = categoria) # Filtramos los posts por las categorias
    return render(request, "productos/categoria.html", {"categoria":categoria, "empleados":empleados}) """