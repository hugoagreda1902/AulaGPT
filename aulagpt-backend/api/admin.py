from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('correo', 'nombre_usuario', 'nombre', 'apellido', 'activo', 'es_staff')

admin.site.register(Usuario, UsuarioAdmin)
