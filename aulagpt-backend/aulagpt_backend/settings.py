import os
from pathlib import Path
import environ

# Inicializar environ y leer .env
env = environ.Env()
environ.Env.read_env()

# Seguridad
SECRET_KEY = env('DJANGO_SECRET_KEY', default='fk5dd=8&!c(0on=y6hhhd6hftjq(i)krxv=c45f6tqj$t@uvet')
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['aulagpt.net', 'www.aulagpt.net', '127.0.0.1']

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DATABASE', default='aulagpt_db'),
        'USER': env('MYSQL_USER', default='root'),
        'PASSWORD': env('MYSQL_PASSWORD', default='1234'),
        'HOST': env('MYSQL_HOST', default='127.0.0.1'),
        'PORT': env('MYSQL_PORT', default='3306'),
    }
}


# Configuración de URL raíz
ROOT_URLCONF = 'aulagpt_backend.urls'  

# Autenticación
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'api.User'

# Archivos estáticos y media
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
    'corsheaders.middleware.CorsMiddleware',
]

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'corsheaders',
    'api',
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # Agrega otros orígenes si es necesario
]

# Auto campo por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Localización
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True
