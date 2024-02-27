
import datetime
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from productos.models import Producto, CategoriaProd
from servicios.models import Servicio
from datetime import datetime
from .permissions import *
from django.contrib.auth.models import Permission
from .form import *
from django.contrib import messages

def permiso_denegado(request):
    return render(request, "denegado/permiso_denegado.html")

#Trabajando con usuarios
@custom_permission_required("auth.view_user", redirect_url='administrador:permisoDenegado')
def user(request):
    users = User.objects.all()
    return render(request, "usuarios/usuarios.html", {"users": users})

@custom_permission_required("auth.change_user", redirect_url='administrador:permisoDenegado')
def edit_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)  # Si tienes un formulario de edición, pásale los datos y la instancia del usuario
        if form.is_valid():
            form.save()
            return redirect('administrador:usuarios')  # Redirige a la vista de lista de usuarios o a donde quieras
    else:
        form = UserEditForm(instance=user)  # Si es una solicitud GET, crea una instancia del formulario con los datos actuales del usuario
    
    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'user': user})

@custom_permission_required("auth.delete_user", redirect_url='administrador:permisoDenegado')
def delete_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('administrador:usuarios')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'usuarios/eliminar_usuario.html', {'user': user})

@custom_permission_required("auth.add_user", redirect_url='administrador:permisoDenegado')
def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            # Verifica si el correo electrónico ya está en uso
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Este correo ya esta en uso, coloca otro!!!')
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.last_login = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
                user.save()
                return redirect('administrador:usuarios')
    else:
        form = UserAddForm()

    template = 'usuarios/agregar_usuario.html'
    return render(request, template, {'form': form})




#Trabajando con roles
@custom_permission_required("auth.view_permission", redirect_url='administrador:permisoDenegado')
def rol(request):

    # Obtener una lista de usuarios con sus permisos
    users_with_permissions = User.objects.prefetch_related('user_permissions').all()

    context = {
        'users_with_permissions': users_with_permissions
    }

    return render(request, 'roles/usuarios_roles.html', context)

def rolUser(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Obtener el usuario o mostrar 404 si no existe

    # Obtener los permisos del usuario
    user_permissions = user.user_permissions.all()

    context = {
        'selected_user': user,
        'user_permissions': user_permissions
    }

    return render(request, 'roles/usuario_permisos.html', context)

@custom_permission_required("auth.delete_permission", redirect_url='administrador:permisoDenegado')
def delete_rolUser(request, user_id, permission_id):

    user = User.objects.get(pk=user_id)
    permission = Permission.objects.get(pk=permission_id)

    if request.method == 'POST':
        user.user_permissions.remove(permission)
        return redirect('administrador:roles')
        
    return render(request, 'roles/delete_usuarioPermiso.html', {'user': user, 'permission': permission})

@custom_permission_required("auth.add_permission", redirect_url='administrador:permisoDenegado')
def add_rolUser(request, user_id):
    
    user = get_object_or_404(User, pk=user_id)
    
    all_permissions = Permission.objects.all()
    missing_permissions = all_permissions.exclude(id__in=user.user_permissions.values_list('id', flat=True))

    context = {
        'user': user,
        'missing_permissions': missing_permissions,
    }

    return render(request, 'roles/add_usuarioPermiso.html', context)

def agregarRol(request, user_id, permission_id):

    user = get_object_or_404(User, pk=user_id)
    permission = get_object_or_404(Permission, pk=permission_id)

    # Agrega la relación de permiso al usuario
    user.user_permissions.add(permission)

    context = {
        'selected_user': user,
        'selected_permission':permission,
    }

    return redirect('administrador:roles')



#Trabajando con blogs
@custom_permission_required("auth.view_empleado", redirect_url='administrador:permisoDenegado')
def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/empleados.html', {'empleados': empleados})

@custom_permission_required("auth.edit_empleado", redirect_url='administrador:permisoDenegado')
def edit_empleados(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = EmpleadosEditForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('administrador:empleados')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = EmpleadosEditForm(instance=empleado)

    return render(request, 'empleado/editar_empleados.html', {'form': form, 'empleado': empleado})

@custom_permission_required("auth.delete_empleado", redirect_url='administrador:permisoDenegado')
def delete_empleados(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('administrador:empleados')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'empleado/eliminar_empleados.html', {'empleado': empleado})

@custom_permission_required("auth.add_empleado", redirect_url='administrador:permisoDenegado')
def add_empleados(request):
    if request.method == 'POST':
        form = EmpleadoAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Agrega estas líneas para verificar la imagen que se está recibiendo
            print(request.FILES)  # Deberías ver la información de la imagen en la consola
            empleado = form.save(commit=False)
            empleado.fecha_publicacion = datetime.now()
            empleado.save()
            return redirect('administrador:empleados')
        else:
            print(form.errors)  # Esto te mostrará los errores de validación si los hay
    else:
        form = EmpleadoAddForm()

    template = 'empleado/agregar_empleados.html'
    return render(request, template, {'form': form})



#Trabajando con Categoria empleados
@custom_permission_required("auth.view_categoria", redirect_url='administrador:permisoDenegado')
def categoriasEmpleados(request):
    categoriasEmpleados = CategoriaEmpleado.objects.all()
    return render(request, "empleadosCategorias/categorias.html", {"categoriasEmpleados": categoriasEmpleados})

@custom_permission_required("auth.add_categoria", redirect_url='administrador:permisoDenegado')
def add_categoriasEmpleados(request):
    if request.method == 'POST':
        form = EmpleadoCategoriaAddForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.fecha_publicacion = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            categoria.save()
            return redirect('administrador:empleadosCategorias')
    else:
        form = EmpleadoCategoriaAddForm()

    template = 'empleadosCategorias/agregar_categoria.html'
    return render(request, template, {'form': form})

@custom_permission_required("auth.edit_categoria", redirect_url='administrador:permisoDenegado')
def edit_categoriasEmpleados(request, categoriaEmpleados_id):
    categoria = get_object_or_404(CategoriaEmpleado, id=categoriaEmpleados_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = EmpleadoCategoriaEditForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('administrador:empleadosCategorias')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = EmpleadoCategoriaEditForm(instance=categoria)

    return render(request, 'empleadosCategorias/editar_categoria.html', {'form': form, 'categoria': categoria})



#Trabajando con preguntas 
@custom_permission_required("auth.view_nosotro", redirect_url='administrador:permisoDenegado')
def preguntas(request):
    preguntas = Nosotros.objects.all()
    return render(request, "preguntas/preguntas.html", {"preguntas": preguntas})

@custom_permission_required("auth.add_nosotro", redirect_url='administrador:permisoDenegado')
def add_preguntas(request):
    if request.method == 'POST':
        form = PreguntasAddForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.fecha_publicacion = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            pregunta.save()
            return redirect('administrador:preguntas')
    else:
        form = PreguntasAddForm()

    template = 'preguntas/agregar_preguntas.html'
    return render(request, template, {'form': form})

@custom_permission_required("auth.delete_nosotro", redirect_url='administrador:permisoDenegado')
def delete_preguntas(request, pregunta_id):
    pregunta = get_object_or_404(Nosotros, id=pregunta_id)
    
    if request.method == 'POST':
        pregunta.delete()
        return redirect('administrador:preguntas')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'preguntas/eliminar_preguntas.html', {'pregunta': pregunta}) 

@custom_permission_required("auth.edit_nosotro", redirect_url='administrador:permisoDenegado')
def edit_preguntas(request, pregunta_id):
    pregunta = get_object_or_404(Nosotros, id=pregunta_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = PreguntasEditForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('administrador:preguntas')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = PreguntasEditForm(instance=pregunta)

    return render(request, 'preguntas/editar_preguntas.html', {'form': form, 'pregunta': pregunta})



#Trabajando con servicios
@custom_permission_required("auth.view_servicio", redirect_url='administrador:permisoDenegado')
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicio/servicios.html", {"servicios": servicios})

@custom_permission_required("auth.add_servicio", redirect_url='administrador:permisoDenegado')
def add_servicios(request):
    if request.method == 'POST':
        form = ServicioAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Agrega estas líneas para verificar la imagen que se está recibiendo
            print(request.FILES)  # Deberías ver la información de la imagen en la consola
            servicio = form.save(commit=False)
            servicio.fecha_publicacion = datetime.now()
            servicio.save()
            return redirect('administrador:servicios')
        else:
            print(form.errors)  # Esto te mostrará los errores de validación si los hay
    else:
        form = ServicioAddForm()

    template = 'servicio/agregar_servicio.html'
    return render(request, template, {'form': form})

@custom_permission_required("auth.edit_servicio", redirect_url='administrador:permisoDenegado')
def edit_servicios(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = ServicioEditForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('administrador:servicios')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = ServicioEditForm(instance=servicio)

    return render(request, 'servicio/editar_servicio.html', {'form': form, 'servicio': servicio})

@custom_permission_required("auth.delete_servicio", redirect_url='administrador:permisoDenegado')
def delete_servicios(request, servicio_id):
   
    servicio = get_object_or_404(Servicio, id=servicio_id)
    
    if request.method == 'POST':
        servicio.delete()
        return redirect('administrador:servicios')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'servicio/eliminar_servicio.html', {'servicio': servicio})



#Trabajando con productos
@custom_permission_required("auth.view_producto", redirect_url='administrador:permisoDenegado')
def productos(request):
    productos = Producto.objects.all()
    return render(request, "producto/productos.html", {"productos": productos})
    
@custom_permission_required("auth.add_producto", redirect_url='administrador:permisoDenegado')
def add_productos(request):
    if request.method == 'POST':
        form = ProductoAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Agrega estas líneas para verificar la imagen que se está recibiendo
            print(request.FILES)  # Deberías ver la información de la imagen en la consola
            producto = form.save(commit=False)
            producto.fecha_publicacion = datetime.now()
            producto.save()
            return redirect('administrador:productos')
        else:
            print(form.errors)  # Esto te mostrará los errores de validación si los hay
    else:
        form = ProductoAddForm()

    template = 'producto/agregar_producto.html'
    return render(request, template, {'form': form})

@custom_permission_required("auth.edit_producto", redirect_url='administrador:permisoDenegado')
def edit_productos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = ProductoEditForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrador:productos')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = ProductoEditForm(instance=producto)

    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto})

@custom_permission_required("auth.delete_producto", redirect_url='administrador:permisoDenegado')
def delete_productos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('administrador:productos')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'producto/eliminar_producto.html', {'producto': producto})



#Trabajando con Categoria productos
@custom_permission_required("auth.view_categoriaProd", redirect_url='administrador:permisoDenegado')
def categoriasProd(request):
    categoriasProd = CategoriaProd.objects.all()
    return render(request, "productosCategorias/categorias.html", {"categoriasProd": categoriasProd})

@custom_permission_required("auth.add_categoriaProd", redirect_url='administrador:permisoDenegado')
def add_categoriasProd(request):
    if request.method == 'POST':
        form = ProductoCategoriaAddForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.fecha_publicacion = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            categoria.save()
            return redirect('administrador:productosCategorias')
    else:
        form = ProductoCategoriaAddForm()

    template = 'productosCategorias/agregar_categoria.html'
    return render(request, template, {'form': form})

@custom_permission_required("auth.edit_categoriaProd", redirect_url='administrador:permisoDenegado')
def edit_categoriasProd(request, categoriaProd_id):
    categoria = get_object_or_404(CategoriaProd, id=categoriaProd_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = ProductoCategoriaEditForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('administrador:productosCategorias')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = ProductoCategoriaEditForm(instance=categoria)

    return render(request, 'productosCategorias/editar_categoria.html', {'form': form, 'categoria': categoria})



#Trabajando con sucursales 
@custom_permission_required("auth.view_ubicacion", redirect_url='administrador:permisoDenegado')
def sucursales(request):
    sucursales = Ubicacion.objects.all()
    return render(request, "sucursales/sucursales.html", {"sucursales": sucursales})

@custom_permission_required("auth.add_ubicacion", redirect_url='administrador:permisoDenegado')
def add_sucursales(request):
    if request.method == 'POST':
        form = SucursalesAddForm(request.POST)
        if form.is_valid():
            sucursal = form.save(commit=False)
            sucursal.fecha_publicacion = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            sucursal.save()
            return redirect('administrador:sucursales')
    else:
        form = SucursalesAddForm()

    template = 'sucursales/agregar_sucursales.html'
    return render(request, template, {'form': form})

@custom_permission_required("auth.delete_ubicacion", redirect_url='administrador:permisoDenegado')
def delete_sucursales(request, sucursal_id):
    sucursal = get_object_or_404(Ubicacion, id=sucursal_id)
    
    if request.method == 'POST':
        sucursal.delete()
        return redirect('administrador:sucursales')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'sucursales/eliminar_sucursales.html', {'sucursal': sucursal}) 

@custom_permission_required("auth.edit_ubicacion", redirect_url='administrador:permisoDenegado')
def edit_sucursales(request, sucursal_id):
    sucursal = get_object_or_404(Ubicacion, id=sucursal_id)

    if request.method == 'POST':
        form = SucursalesEditForm(request.POST, request.FILES, instance=sucursal)
        if form.is_valid():
            # Eliminar archivo de imagen anterior si se está actualizando la imagen
            if sucursal.imagen and 'imagen' in request.FILES:
                # Eliminar el archivo antiguo
                if os.path.exists(sucursal.imagen.path):
                    os.remove(sucursal.imagen.path)

            # Guardar el nuevo formulario
            form.save()
            return redirect('administrador:sucursales')  # Redirige a la vista de sucursales después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = SucursalesEditForm(instance=sucursal)

    return render(request, 'sucursales/editar_sucursales.html', {'form': form, 'sucursal': sucursal})



