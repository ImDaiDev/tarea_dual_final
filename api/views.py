from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mensaje

@api_view(['GET'])
def saludo(request):
    return Response({
        "mensaje": "Hola desde la API Django",
        "estado": "OK"
    })

@api_view(['GET'])
def mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-creado_en')
    data = [m.texto for m in mensajes]

    return Response({
        "total": len(data),
        "mensajes": data
    })
