from django.contrib import admin
from django.urls import path
from . import views  # Importar las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página de inicio
]
