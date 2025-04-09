# api/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # Aquí puedes personalizar lo que ves en el admin de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

# Vuelve a registrar el modelo User en el admin para personalizarlo si es necesario
admin.site.unregister(User)  # Primero desregistramos el modelo por defecto
admin.site.register(User, CustomUserAdmin)  # Luego registramos nuestra versión personalizada
