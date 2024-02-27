from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CategoriaEmpleado, Empleado

class CategoriaEmpleadoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(CategoriaEmpleado, CategoriaEmpleadoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)