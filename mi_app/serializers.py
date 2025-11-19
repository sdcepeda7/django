from rest_framework import serializers
from .models import Autor, Libro, Resena

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    # Campo calculado: Nombre del autor (solo lectura)
    nombre_autor = serializers.ReadOnlyField(source='autor.nombre')
    
    # Campo calculado: Las 5 reseñas más recientes
    resenas_recientes = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'fecha_publicacion', 'resumen', 'autor', 'nombre_autor', 'resenas_recientes']

    def get_resenas_recientes(self, obj):
        # Obtiene las reseñas ordenadas por fecha descendente y toma las 5 primeras
        resenas = obj.resenas.order_by('-fecha')[:5]
        return ResenaSerializer(resenas, many=True).data

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'