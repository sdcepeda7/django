from django.http import HttpResponse
from django.db.models import Avg
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer

def saludo(request):
    return HttpResponse(" API de Biblioteca ")

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
    # Configuración de filtros y ordenamiento
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['autor', 'fecha_publicacion'] # Filtrar por autor o fecha
    ordering_fields = ['titulo', 'fecha_publicacion'] # Ordenar por título o fecha

    # Sobreescribimos get_queryset para lógica condicional
    def get_queryset(self):
        queryset = Libro.objects.all()
        # Si la URL tiene ?recent=true, devolvemos los últimos 10 creados (por ID o fecha)
        recent = self.request.query_params.get('recent')
        if recent:
            return queryset.order_by('-id')[:10]
        return queryset

    # Acción personalizada: /api/libros/{id}/promedio_calificacion/
    @action(detail=True, methods=['get'])
    def promedio_calificacion(self, request, pk=None):
        libro = self.get_object()
        # Calculamos el promedio de las reseñas asociadas
        avg = libro.resenas.aggregate(Avg('calificacion'))['calificacion__avg']
        return Response({'promedio_calificacion': avg})

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['libro', 'calificacion']
    ordering_fields = ['calificacion', 'fecha']