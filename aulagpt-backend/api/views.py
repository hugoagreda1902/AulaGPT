from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Class, UserClass, Documents, Tests, TestQuestion, TestAnswer, Activity
from .serializers import (
    UserSerializer, ClassSerializer, UserClassSerializer,
    DocumentsSerializer, TestsSerializer, TestQuestionSerializer,
    TestAnswerSerializer, ActivitySerializer
)
from .serializers import DocumentsSerializer
from .google_drive.utils import subir_a_google_drive 


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            print(f"Usuario encontrado: {user}")  # o logging.info(...)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            return Response({"message": "Login exitoso", "user_id": user.user_id})
        else:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)

        
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        email = request.data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({'email': 'Este email ya está registrado.'}, status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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

            # Llamamos a la función para subir a Google Drive y obtener el link
            drive_link = subir_a_google_drive(uploaded_file)

            # Creamos el documento en la BD
            document = Documents.objects.create(
                drive_link=drive_link,
                file_name=uploaded_file.name,
                file_type=uploaded_file.content_type,
                class_id=serializer.validated_data.get('class_id')
            )

            return Response(DocumentsSerializer(document).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ ViewSets para el resto de modelos
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class UserClassViewSet(viewsets.ModelViewSet):
    queryset = UserClass.objects.all()
    serializer_class = UserClassSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class TestsViewSet(viewsets.ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer

class TestQuestionViewSet(viewsets.ModelViewSet):
    queryset = TestQuestion.objects.all()
    serializer_class = TestQuestionSerializer

class TestAnswerViewSet(viewsets.ModelViewSet):
    queryset = TestAnswer.objects.all()
    serializer_class = TestAnswerSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
