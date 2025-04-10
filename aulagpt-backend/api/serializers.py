from rest_framework import serializers
from django.contrib.auth.models import User  # Importa el modelo User de Django

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Utilizamos el modelo User de Django
        fields = ['id', 'username', 'first_name', 'last_name', 'email']  # Los campos que quieres mostrar
