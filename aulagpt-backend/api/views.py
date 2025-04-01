# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from .models import Usuario

class UsuarioListView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
