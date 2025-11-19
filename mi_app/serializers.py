from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'