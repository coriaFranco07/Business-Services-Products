from django.urls import path
from nosotros import views

app_name = 'nosotros'

urlpatterns = [
    
    path('nosotros/', views.nosotros, name="nosotros"),
    
]
