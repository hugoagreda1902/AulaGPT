import os
from pathlib import Path
import environ
from dotenv import load_dotenv

# Lee el archivo .env
env = environ.Env()
environ.Env.read_env()

# Seguridad
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')  # Usa 'default_secret_key' solo para pruebas locales
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Dirección del sitio (AGREGADO PARA ALLOWED_HOSTS)
ALLOWED_HOSTS = ['aulagpt.net', 'www.aulagpt.net']

# Ruta de base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()  # Carga las variables del .env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'aulagpt_db'),  # Nombre de la base de datos
        'USER': os.getenv('MYSQL_USER', 'root'),             # Usuario MySQL
        'PASSWORD': os.getenv('MYSQL_PASSWORD', '1234'),     # Contraseña del usuario
        'HOST': '127.0.0.1',                                 # Dirección local para Fly.io
        'PORT': '3306',                                      # Puerto de MySQL
    }
}

# Autenticación
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Archivos estáticos y de medios
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    'corsheaders.middleware.CorsMiddleware',  # Middleware para CORS
]

# URL de redirección después de iniciar sesión
LOGIN_REDIRECT_URL = '/'

# URL de redirección después de cerrar sesión
LOGOUT_REDIRECT_URL = '/'

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin', # Panel de administración
    'django.contrib.auth', # Autenticación
    'django.contrib.contenttypes', # Tipos de contenido
    'django.contrib.sessions', # Sesiones
    'django.contrib.messages', # Mensajes
    'django.contrib.staticfiles', # Archivos estáticos
    # Otras apps de tu proyecto
    'rest_framework', # Django REST Framework
    'corsheaders',  # Para manejar CORS
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
