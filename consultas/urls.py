from django.urls import path
from consultas import views

app_name = 'consultas'

urlpatterns = [
    
    path('', views.contacto, name="consultas"),
    
]
