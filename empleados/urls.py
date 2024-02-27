from django.urls import path
from empleados import views

app_name = 'empleado'

urlpatterns = [
    
    path('', views.empleado, name="empleado"),
   
]
