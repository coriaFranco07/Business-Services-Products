from django import forms
from productos.models import Producto, CategoriaProd
from empleados.models import Empleado, CategoriaEmpleado
from servicios.models import Servicio
from nosotros.models import Nosotros, Ubicacion
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password' , 'email'] 
        
class UserAddForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']    




class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categorias', 'imagen', 'precio', 'disponibilidad']
        
class ProductoAddForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'categorias', 'imagen', 'precio', 'disponibilidad']    

class ProductoCategoriaAddForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = ['nombre']

class ProductoCategoriaEditForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = ['nombre']




class EmpleadosEditForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'categorias', 'imagen']

class EmpleadoAddForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'categorias', 'imagen']

class EmpleadoCategoriaAddForm(forms.ModelForm):
    class Meta:
        model = CategoriaEmpleado
        fields = ['nombre']

class EmpleadoCategoriaEditForm(forms.ModelForm):
    class Meta:
        model = CategoriaEmpleado
        fields = ['nombre']




class ServicioAddForm(forms.ModelForm):
   class Meta:
        model = Servicio
        fields = ['titulo', 'contenido', 'imagen']

class ServicioEditForm(forms.ModelForm):
    class Meta:
            model = Servicio
            fields = ['titulo', 'contenido', 'imagen']




class PreguntasAddForm(forms.ModelForm):
    class Meta:
        model = Nosotros
        fields = ['titulo', 'contenido']

class PreguntasEditForm(forms.ModelForm):
    class Meta:
        model = Nosotros
        fields = ['titulo', 'contenido']




class SucursalesAddForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['ubicacion', 'imagen']

class SucursalesEditForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['ubicacion', 'imagen']