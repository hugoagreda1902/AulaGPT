import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import pymysql
pymysql.install_as_MySQLdb()

load_dotenv()  # Carga las variables de entorno desde el archivo .env


BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles/frontend')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de la clave secreta
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default_secret_key')

# Configuración de modo de depuración
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Hosts permitidos (separados por comas)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aulagpt_db',  # Asegúrate de que este nombre coincida
        'USER': 'root',  # Reemplaza con tu nombre de usuario de MySQL
        'PASSWORD': '1234',  # Reemplaza con tu contraseña
        'HOST': 'localhost',  # O la IP del servidor si no está local
        'PORT': '3306',  # El puerto por defecto de MySQL
    }
}


# Root URL configuration
ROOT_URLCONF = 'aula_gpt_backend.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

