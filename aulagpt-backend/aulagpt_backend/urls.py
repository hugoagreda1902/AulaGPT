from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView

def home(request):
    return JsonResponse({"message": "API AulaGPT funcionando"})

urlpatterns = [
    path('', home),  # Ruta raíz /
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Enlaza las urls de tu app 'api'
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

