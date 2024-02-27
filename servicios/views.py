from django.http import JsonResponse
from django.shortcuts import render
import requests
from .models import Servicio

# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})


def mi_vista(request):
    url_api = 'https://dolarapi.com/v1/dolares/blue'  # Reemplaza esto con la URL de la API que deseas consumir
    
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url_api)
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
        
        datos = response.json()  # Convertir la respuesta a JSON
        
        # Devolver los datos como una respuesta JSON
        return JsonResponse(datos)
        
    except requests.exceptions.RequestException as e:
        # Manejar errores si la solicitud no fue exitosa
        error_message = 'Error al obtener datos de la API: ' + str(e)
        return JsonResponse({'error': error_message}, status=500)