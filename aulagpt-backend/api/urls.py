# aulagpt-backend/urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración
    # Aquí puedes agregar otras rutas si tienes otras vistas personalizadas
]
