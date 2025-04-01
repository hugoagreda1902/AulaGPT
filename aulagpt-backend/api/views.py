# api/views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Obtiene todos los usuarios
    serializer_class = UserSerializer  # Usa el serializador para devolver los datos
