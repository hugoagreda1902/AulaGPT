# api/views.py
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User  # Asegúrate de importar el modelo User

class UsuarioListView(ListView):
    model = User
    template_name = 'api/usuarios_list.html'  # Aquí la ruta debe ser sin la carpeta 'templates' ya que Django ya sabe buscar en esa carpeta
    context_object_name = 'usuarios'