import os
from django.core.wsgi import get_wsgi_application

# Establecer la configuración de Django para producción
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Exponer la aplicación WSGI
application = get_wsgi_application()
