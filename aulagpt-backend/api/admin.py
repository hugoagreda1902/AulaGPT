from django.contrib import admin
from .models import User  # Importa el modelo User desde models.py

# Registra el modelo User en el panel de administración de Django
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de usuarios en el admin
    list_display = ('user_id', 'name', 'surname', 'email', 'role')
    # Permite buscar usuarios por nombre, apellido o correo electrónico
    search_fields = ('name', 'surname', 'email')
    # Añade un filtro lateral para filtrar usuarios según su rol (student o teacher)
    list_filter = ('role',)
