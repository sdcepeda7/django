from django.http import HttpResponse
from rest_framework import viewsets
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer

def saludo(request):
    return HttpResponse("Sistema de Biblioteca activo.")

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer