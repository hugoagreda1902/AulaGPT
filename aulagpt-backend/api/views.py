from rest_framework import viewsets, status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User, Class, UserClass, Documents, Tests, TestQuestion, TestAnswer, Activity
from .serializers import (
    RegisterSerializer, UserSerializer, DocumentsSerializer, ClassSerializer, UserClassSerializer,
    DocumentsSerializer, TestsSerializer, TestQuestionSerializer,
    TestAnswerSerializer, ActivitySerializer
)
from .google_drive.utils import subir_a_google_drive

from django.db import connection
import time

@ api_view(['GET'])
@permission_classes([AllowAny])
def ping_db(request):
    start = time.time()
    try:
        connection.ensure_connection()
        status = "OK"
    except Exception as e:
        status = f"ERROR: {e}"
    elapsed = time.time() - start
    return Response({"db_status": status, "elapsed": elapsed})

# ✅ Vista protegida con autenticación JWT
class MiVistaProtegida(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"mensaje": f"Hola, {request.user.username}"})


# ✅ Gestión de usuarios
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'register':
            return RegisterSerializer
        return UserSerializer

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Registro exitoso",
                "user_id": user.user_id,
                "email": user.email,
                "role": user.role
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            return Response({
                "message": "Login exitoso",
                "user_id": user.user_id
            })
        else:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ Gestión de documentos con subida a Google Drive
class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = DocumentsSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = request.FILES.get('file')

            if not uploaded_file:
                return Response({'file': 'Archivo requerido.'}, status=status.HTTP_400_BAD_REQUEST)

            # 📤 Subir archivo a Google Drive
            drive_link = subir_a_google_drive(uploaded_file)

            # 📦 Guardar documento en la base de datos
            document = Documents.objects.create(
                drive_link=drive_link,
                file_name=uploaded_file.name,
                file_type=uploaded_file.content_type,
                class_id=serializer.validated_data.get('class_id')
            )

            return Response(DocumentsSerializer(document).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadDocumentView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Asocia el documento al usuario que lo sube
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Gestión de clases
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Asociación entre usuario y clase
class UserClassViewSet(viewsets.ModelViewSet):
    queryset = UserClass.objects.all()
    serializer_class = UserClassSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# ✅ Tests, preguntas, respuestas y actividad
class TestsViewSet(viewsets.ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestQuestionViewSet(viewsets.ModelViewSet):
    queryset = TestQuestion.objects.all()
    serializer_class = TestQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestAnswerViewSet(viewsets.ModelViewSet):
    queryset = TestAnswer.objects.all()
    serializer_class = TestAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
