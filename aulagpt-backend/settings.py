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
ROOT_URLCONF = 'urls'  # Nombre de tu proyecto y archivo urls.py

# Autenticación
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'api.Usuario'


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
    'corsheaders.middleware.CorsMiddleware', # Middleware para CORS
]

INSTALLED_APPS = [
    # Django apps que no creas tablas en la base de datos
    'django.contrib.admin',  # Para administración (si la necesitas)
    'django.contrib.auth',  # Si quieres usar autenticación
    'django.contrib.contenttypes',  # Para gestionar tipos de contenido
    'django.contrib.sessions',  # Si vas a usar sesiones (por ejemplo, autenticación)
    'django.contrib.messages',  # Para manejo de mensajes
    'django.contrib.staticfiles',  # Si vas a manejar archivos estáticos
    'corsheaders',  # Para CORS, si lo necesitas
    'api',  # Tu propia aplicación (cambia 'api' por el nombre de tu app)
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # Agrega otras URLs si es necesario
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


TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True
