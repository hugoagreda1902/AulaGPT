from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Class, UserClass, Documents, Tests, TestQuestion, TestAnswer, Activity
from .serializers import (
    UserSerializer, ClassSerializer, UserClassSerializer,
    DocumentsSerializer, TestsSerializer, TestQuestionSerializer,
    TestAnswerSerializer, ActivitySerializer
)

# ✅ ViewSet personalizado para el registro de usuarios
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

# ✅ ViewSets para el resto de modelos
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class UserClassViewSet(viewsets.ModelViewSet):
    queryset = UserClass.objects.all()
    serializer_class = UserClassSerializer

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

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
