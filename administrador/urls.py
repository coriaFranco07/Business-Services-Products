from django.urls import path
from . import views

app_name = 'administrador'

urlpatterns = [

    path('permisoDenegado/', views.permiso_denegado, name='permisoDenegado'),

    path('producto/', views.productos, name='productos'),
    path('editProducto/<int:producto_id>/', views.edit_productos, name='productoEdit'),
    path('deleteProducto/<int:producto_id>/', views.delete_productos, name='productoDelete'),
    path('addProducto/', views.add_productos, name='productoAdd'),

    path('productosCategorias/', views.categoriasProd, name='productosCategorias'),
    path('addProductosCategoria/', views.add_categoriasProd, name='productosCategoriaAdd'),
    path('editProductosCategoria/<int:categoriaProd_id>/', views.edit_categoriasProd, name='productosCategoriaEdit'),

    path('usuarios/', views.user, name='usuarios'),
    path('editUsuarios/<int:user_id>/', views.edit_user, name='usuariosEdit'),
    path('deleteUsuarios/<int:user_id>/', views.delete_user, name='usuariosDelet'),
    path('addUsuarios/', views.add_user, name='usuariosAdd'),

    path('empleados/', views.empleados, name='empleados'),
    path('editEmpleados/<int:empleado_id>/', views.edit_empleados, name='empleadosEdit'),
    path('deleteEmpleados/<int:empleado_id>/', views.delete_empleados, name='empleadosDelet'),
    path('addEmpleados/', views.add_empleados, name='empleadosAdd'),

    path('empleadosCategorias/', views.categoriasEmpleados, name='empleadosCategorias'),
    path('addEmpleadoCategoria/', views.add_categoriasEmpleados, name='empleadoCategoriaAdd'),
    path('editEmpleadoCategoria/<int:categoriaEmpleados_id>/', views.edit_categoriasEmpleados, name='empleadoCategoriaEdit'),


    path('servicios/', views.servicios, name='servicios'),
    path('editServicio/<int:servicio_id>/', views.edit_servicios, name='servicioEdit'),
    path('deleteServicio/<int:servicio_id>/', views.delete_servicios, name='servicioDelete'),
    path('addServicio/', views.add_servicios, name='servicioAdd'),


    path('preguntas/', views.preguntas, name='preguntas'),
    path('editPreguntas/<int:pregunta_id>/', views.edit_preguntas, name='preguntaEdit'),
    path('deletePreguntas/<int:pregunta_id>/', views.delete_preguntas, name='preguntaDelete'),
    path('addPreguntas/', views.add_preguntas, name='preguntaAdd'),


    path('sucursales/', views.sucursales, name='sucursales'),
    path('editSucursales/<int:sucursal_id>/', views.edit_sucursales, name='sucursalEdit'),
    path('deleteSucursales/<int:sucursal_id>/', views.delete_sucursales, name='sucursalDelete'),
    path('addSucursales/', views.add_sucursales, name='sucursalAdd'),


    path('roles/', views.rol, name='roles'),
    path('rolesUsuario/<int:user_id>/', views.rolUser, name='rolesUsuario'),
    path('eliminarRolesUsuario/<int:user_id>/<int:permission_id>/', views.delete_rolUser, name='rolesUsuarioDelet'),
    path('agregarRolesUsuario/<int:user_id>/', views.add_rolUser, name='rolesUsuarioAdd'),
    path('agregarRol/<int:user_id>/<int:permission_id>', views.agregarRol, name='agregarPermiso'),
    

   
    
      
]
