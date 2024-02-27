from django.db import models

# Create your models here.
class Nosotros(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='nosotro'
        verbose_name_plural='nosotros'

    def __str__(self):
        return self.titulo 
    

class Ubicacion(models.Model):
    ubicacion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="ubicacion", null=False, blank=False, default="ubicacion/9318694.jpg")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='ubicacion'
        verbose_name_plural='ubicaciones'

    def __str__(self):
        return self.ubicacion 

