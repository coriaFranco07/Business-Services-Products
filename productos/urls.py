from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [

path('', views.producto, name="producto"),
path('categoria/<str:categoria_slug>/', views.categoria, name="categoria")

]