from django.http import HttpResponseRedirect
from django.urls import reverse

def custom_permission_required(permission, redirect_url, raise_exception=False):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.has_perm(permission):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse(redirect_url))
        return _wrapped_view
    return decorator


# Permisos usuarios
""" view_user_permission = permission_required("auth.view_user", raise_exception=True, login_url='administrador:permisoDenegado')
edit_user_permission = permission_required("auth.change_user", raise_exception=True)
delete_user_permission = permission_required("auth.delete_user", raise_exception=True)
add_user_permission = permission_required("auth.add_user", raise_exception=True) """

# Roles
""" view_rol_permission = permission_required("auth.view_permission", raise_exception=True)
add_rol_permission = permission_required("auth.add_permission", raise_exception=True)
delete_rol_permission = permission_required("auth.delete_permission", raise_exception=True) """


""" #Empleado
view_empleado_permission = permission_required("auth.view_empleado", raise_exception=True)
edit_empleado_permission = permission_required("auth.change_empleado", raise_exception=True)
delete_empleado_permission = permission_required("auth.delete_empleado", raise_exception=True)
add_empleado_permission = permission_required("auth.add_empleado", raise_exception=True)


#Empleado Categorias
view_categoria_permission = permission_required("auth.view_categoria", raise_exception=True)
edit_categoria_permission = permission_required("auth.change_categoria", raise_exception=True)
add_categoria_permission = permission_required("auth.add_categoria", raise_exception=True)


#Servivios
view_servicio_permission = permission_required("auth.view_servicio", raise_exception=True)
edit_servicio_permission = permission_required("auth.change_servicio", raise_exception=True)
delete_servicio_permission = permission_required("auth.delete_servicio", raise_exception=True)
add_servicio_permission = permission_required("auth.add_servicio", raise_exception=True)


#Productos
view_producto_permission = permission_required("auth.view_producto", raise_exception=True)
edit_producto_permission = permission_required("auth.change_producto", raise_exception=True)
delete_producto_permission = permission_required("auth.delete_producto", raise_exception=True)
add_producto_permission = permission_required("auth.add_producto", raise_exception=True)


#Categoria Categorias
view_categoriaProd_permission = permission_required("auth.view_categoriaProd", raise_exception=True)
edit_categoriaProd_permission = permission_required("auth.change_categoriaProd", raise_exception=True)
add_categoriaProd_permission = permission_required("auth.add_categoriaProd", raise_exception=True)


#Pregunatas
view_pregunta_permission = permission_required("auth.view_nosotro", raise_exception=True)
edit_pregunta_permission = permission_required("auth.change_nosotro", raise_exception=True)
delete_pregunta_permission = permission_required("auth.delete_nosotro", raise_exception=True)
add_pregunta_permission = permission_required("auth.add_nosotro", raise_exception=True)


#Sucursales
view_sucursal_permission = permission_required("auth.view_ubicacion", raise_exception=True)
edit_sucursal_permission = permission_required("auth.change_ubicacion", raise_exception=True)
delete_sucursal_permission = permission_required("auth.delete_ubicacion", raise_exception=True)
add_sucursal_permission = permission_required("auth.add_ubicacion", raise_exception=True) """