# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)  # Registra las rutas para el modelo User

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el router
]
