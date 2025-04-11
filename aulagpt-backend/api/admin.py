# api/admin.py

from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'correo', 'nombre', 'apellido', 'edad', 'telefono')  # Campos que se mostrarán en la lista
    search_fields = ['usuario', 'correo']  # Campos por los cuales se podrá buscar
    list_filter = ('edad',)  # Filtros por edad, por ejemplo
    ordering = ['usuario']  # Orden por el campo 'usuario'

admin.site.register(Usuario, UsuarioAdmin)  # Registrar el modelo 'Usuario' con su personalización
