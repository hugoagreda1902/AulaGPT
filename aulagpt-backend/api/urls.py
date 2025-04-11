from django.urls import path
from .views import UsuarioList

urlpatterns = [
    path('api/usuarios/', UsuarioList.as_view(), name='usuario-list'),
]
