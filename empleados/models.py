from django.db import models

# Create your models here.

class CategoriaEmpleado(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre 
    

class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaEmpleado, on_delete=models.CASCADE, default=1) # Establecemos relacion con Categoria
    imagen=models.ImageField(upload_to="empleado", null=False, blank=False, default="empleado/imagen_admin.png")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='empleado'
        verbose_name_plural='empleados'

    def __str__(self):
        return self.nombre 