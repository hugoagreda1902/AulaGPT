import os
from pathlib import Path
import environ
from dotenv import load_dotenv

# Lee el archivo .env
env = environ.Env()
environ.Env.read_env()

# Seguridad
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['aulagpt.net', 'www.aulagpt.net', '127.0.0.1']

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()



# Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'aulagpt_db'),
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', '1234'),
        'HOST': os.getenv('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.getenv('MYSQL_PORT', '3306'),
    }
}

# Configuración de URL
ROOT_URLCONF = 'api.urls'  # Nombre de tu proyecto y archivo urls.py

# Autenticación
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Archivos estáticos y de medios
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

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

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'django.contrib.auth',       # Para la autenticación
    'django.contrib.contenttypes',  # Necesario para el sistema de permisos de Django
    'django.contrib.sessions',   # Para el manejo de sesiones
    'django.contrib.messages',   # Para mostrar mensajes a los usuarios
    'django.contrib.admin',      # Si quieres usar el admin de Django
    'api',  # Tu app personalizada
]




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

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True
