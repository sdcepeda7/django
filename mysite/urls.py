from django.contrib import admin
from django.urls import path, include # ¡Añade include!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')), # Le dice a Django que busque las URLs en mi_app
]