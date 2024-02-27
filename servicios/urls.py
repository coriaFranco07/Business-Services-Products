from django.urls import path
from servicios import views

app_name = 'servicio'

urlpatterns = [

    path('', views.servicios, name="servicio"),
    path('api/', views.mi_vista, name="api"),

    
]
