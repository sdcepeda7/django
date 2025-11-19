from mi_app.models import Autor, Libro, Resena
from datetime import date

# Opcional: Limpiar datos anteriores para evitar duplicados al probar
print("Limpiando datos existentes...")
Resena.objects.all().delete()
Libro.objects.all().delete()
Autor.objects.all().delete()

print("Creando autores...")
# Creamos instancias de Autor
autor_garcia = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombiana")
autor_rowling = Autor.objects.create(nombre="J.K. Rowling", nacionalidad="Británica")
autor_orwell = Autor.objects.create(nombre="George Orwell", nacionalidad="Británica")

print("Creando libros...")
# Creamos instancias de Libro asociadas a los autores
libro_cien = Libro.objects.create(
    titulo="Cien años de soledad",
    fecha_publicacion=date(1967, 5, 30),
    resumen="La historia de la familia Buendía en el pueblo ficticio de Macondo.",
    autor=autor_garcia
)

libro_amor = Libro.objects.create(
    titulo="El amor en los tiempos del cólera",
    fecha_publicacion=date(1985, 1, 1),
    resumen="La historia de amor entre Fermina Daza y Florentino Ariza.",
    autor=autor_garcia
)

libro_harry = Libro.objects.create(
    titulo="Harry Potter y la piedra filosofal",
    fecha_publicacion=date(1997, 6, 26),
    resumen="Un niño descubre que es un mago y asiste a una escuela de magia.",
    autor=autor_rowling
)

libro_1984 = Libro.objects.create(
    titulo="1984",
    fecha_publicacion=date(1949, 6, 8),
    resumen="Una novela distópica sobre el totalitarismo y la vigilancia masiva.",
    autor=autor_orwell
)

print("Creando reseñas...")
# Creamos reseñas asociadas a los libros
Resena.objects.create(
    texto="Una obra maestra absoluta del realismo mágico.",
    calificacion=5,
    libro=libro_cien
)

Resena.objects.create(
    texto="Un poco difícil de seguir con tantos Aurelianos, pero vale la pena.",
    calificacion=4,
    libro=libro_cien
)

Resena.objects.create(
    texto="Un clásico moderno que marcó mi infancia.",
    calificacion=5,
    libro=libro_harry
)

Resena.objects.create(
    texto="Aterradoramente profética.",
    calificacion=5,
    libro=libro_1984
)

print("¡Datos poblados exitosamente!")