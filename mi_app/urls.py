from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet, basename='autor')
router.register(r'libros', views.LibroViewSet, basename='libro')
router.register(r'resenas', views.ResenaViewSet, basename='resena')

urlpatterns = [
    path('', views.saludo, name='saludo'),
    path('api/', include(router.urls)),
]