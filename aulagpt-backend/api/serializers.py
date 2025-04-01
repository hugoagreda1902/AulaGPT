# api/serializers.py
from rest_framework import serializers
from .models import User  # Asegúrate de importar el modelo adecuado

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # El modelo de tu tabla de usuarios
        fields = ['id', 'nombre', 'correo', 'password']  # Los campos que deseas exponer
