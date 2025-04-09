# api/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Usuario  # Asegúrate de importar tu modelo correctamente

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'  # Nombre del archivo de plantilla
    context_object_name = 'usuarios'  # Nombre que tendrá la lista de usuarios en el contexto
