import os
from pathlib import Path
import dj_database_url

# Seguridad
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')  # Usa 'default_secret_key' solo para pruebas locales
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Dirección del sitio (AGREGADO PARA ALLOWED_HOSTS)
ALLOWED_HOSTS = ['aula-gpt.net', 'www.aula-gpt.net']

# Ruta de base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de la base de datos
DATABASE_URL = os.getenv('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL', 'mysql://root:1234@localhost:3306/aulagpt_db'))
}


# Autenticación
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Archivos estáticos y de medios (modificar según lo necesario)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Middleware (opciones de seguridad adicionales)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL de redirección después de iniciar sesión
LOGIN_REDIRECT_URL = '/'

# URL de redirección después de cerrar sesión
LOGOUT_REDIRECT_URL = '/'

# Aplicaciones instaladas (verifica las aplicaciones de tu proyecto)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Otras apps de tu proyecto
]

# Plantillas y configuraciones adicionales
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de la zona horaria
TIME_ZONE = 'UTC'

# Configuración de la lengua
LANGUAGE_CODE = 'en-us'

# Configuración de la base de datos para sesiones, caché, etc.
USE_I18N = True
USE_L10N = True
USE_TZ = True
