from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    resumen = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    texto = models.TextField()
    # CAMBIO: FloatField con validadores de 0.0 a 5.0 
    calificacion = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    fecha = models.DateTimeField(auto_now_add=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"