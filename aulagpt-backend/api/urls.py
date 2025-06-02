from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ClassViewSet, UserClassViewSet,
    DocumentsViewSet, TestsViewSet, TestQuestionViewSet,
    TestAnswerViewSet, ActivityViewSet,
)

# Creamos un router por defecto de DRF para gestionar las rutas automáticamente
router = DefaultRouter()

# Registramos cada ViewSet con un prefijo en la URL
router.register(r'users', UserViewSet, basename='user')                       # Rutas para gestionar usuarios
router.register(r'classes', ClassViewSet)
router.register(r'userclasses', UserClassViewSet)
router.register(r'documents', DocumentsViewSet, basename='documents')
router.register(r'tests', TestsViewSet)
router.register(r'testquestions', TestQuestionViewSet)
router.register(r'testanswers', TestAnswerViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]