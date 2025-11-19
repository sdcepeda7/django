Proyecto de Gestión de Biblioteca (Django)

Este proyecto es una aplicación web desarrollada en Django para la gestión de una biblioteca. Permite administrar Autores, Libros y Reseñas a través del panel de administración de Django y expone una API REST básica para consultar estos datos.

Proyecto realizado para la asignatura de Programación Web de la Universidad Francisco de Paula Santander.

📋 Características

Modelos Relacionales: Autores, Libros y Reseñas correctamente vinculados.

Panel de Administración: Interfaz completa para CRUD (Crear, Leer, Actualizar, Borrar).

API REST: Endpoints para consultar la información en formato JSON.

Script de Poblado: Automatización para cargar datos de prueba rápidamente.

🚀 Instrucciones de Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1. Clonar el repositorio

Descarga el código fuente a tu computadora:

git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>


2. Crear un entorno virtual (Opcional pero recomendado)

Es buena práctica aislar las dependencias del proyecto:

# En Windows
python -m venv venv
.\venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate


3. Instalar dependencias

Instala Django y Django REST Framework:

pip install -r requirements.txt


(Si no tienes el archivo requirements.txt, ejecuta: pip install django djangorestframework)

4. Aplicar migraciones

Crea la base de datos inicial (SQLite por defecto):

python manage.py makemigrations
python manage.py migrate


5. Crear un Superusuario

Para poder acceder al panel de administración:

python manage.py createsuperuser


Sigue las instrucciones en pantalla para definir tu usuario y contraseña.

6. Cargar datos de prueba (Script)

El proyecto incluye un script (poblar_datos.py) para llenar la base de datos automáticamente.

En Windows (PowerShell/CMD):

python manage.py shell
>>> exec(open('poblar_datos.py', encoding='utf-8').read())
>>> exit()


En Mac/Linux/Git Bash:

python manage.py shell < poblar_datos.py


7. Ejecutar el servidor

Inicia el servidor de desarrollo:

python manage.py runserver


🌐 Uso

Una vez el servidor esté corriendo, puedes acceder a:

Panel de Administración: http://127.0.0.1:8000/admin/

API Root: http://127.0.0.1:8000/api/

Lista de Libros: http://127.0.0.1:8000/api/libros/


