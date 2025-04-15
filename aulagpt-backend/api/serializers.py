from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('correo', 'nombre_usuario', 'nombre', 'apellido', 'activo', 'es_staff')
