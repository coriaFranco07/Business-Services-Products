import random
import string
from django.db import models
from django.utils.text import slugify

# Create your models here.
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)  # SlugField permite valores en blanco
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generar un slug basado en el nombre, una cadena aleatoria y el ID del objeto
        if not self.slug:
            base_slug = slugify(self.nombre)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            object_id = str(self.id)
            self.slug = f"{base_slug}-{random_string}-{object_id}"
        super(CategoriaProd, self).save(*args, **kwargs)


    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre 
    

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ManyToManyField(CategoriaProd) # Establecemos relacion con Categoria
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre 