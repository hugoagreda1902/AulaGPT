import os
from pathlib import Path
import environ
from dotenv import load_dotenv

# Lee el archivo .env
env = environ.Env()
environ.Env.read_env()
load_dotenv()

# Seguridad
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['aulagpt.net', 'www.aulagpt.net', '127.0.0.1']

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

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
    'django.contrib.admin.middleware.AdminMiddleware',  # Este es el middleware para el admin
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  # Tu app
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Para evitar warnings en migraciones

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Este es el directorio base donde están tus plantillas
        ],
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

# Configuración para personalizar el modelo de usuario
AUTH_USER_MODEL = 'api.Usuario'  # Asegúrate de que esté apuntando a tu modelo Usuario

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True
