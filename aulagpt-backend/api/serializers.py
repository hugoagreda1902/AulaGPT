# api/serializers.py
from rest_framework import serializers
from .models import Usuario  # Importa tu modelo

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Incluye todos los campos del modelo
