from django.urls import path
from . import views  # Asegúrate de que las vistas están importadas correctamente
from .views import UsuarioListView  # Asegúrate de que esta vista existe en views.py

urlpatterns = [
    # Aquí agregas las rutas correspondientes a tus vistas
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
]
