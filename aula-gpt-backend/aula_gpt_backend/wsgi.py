"""
WSGI config for aula_gpt_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Establecer la configuración de Django para producción
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aula-gpt-backend.aula_gpt_backend.settings')

# Exponer la aplicación WSGI
application = get_wsgi_application()
