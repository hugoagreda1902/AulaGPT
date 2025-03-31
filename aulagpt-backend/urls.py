from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin de Django
    path('api/', include('AULAGPT.urls')),  # Enlaza las rutas de la app principal
]
