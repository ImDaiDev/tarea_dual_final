from django.urls import path
from .views import saludo, mensajes

urlpatterns = [
    path('saludo/', saludo),
    path('mensajes/', mensajes),
]
