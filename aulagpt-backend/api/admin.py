from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'correo', 'nombre', 'apellido', 'edad', 'telefono')
    search_fields = ['usuario', 'correo']

admin.site.register(Usuario, UsuarioAdmin)
