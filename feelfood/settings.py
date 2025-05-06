import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Bazaviy yo'l
BASE_DIR = Path(__file__).resolve().parent.parent

# .env faylni yuklash
load_dotenv(BASE_DIR / '.env')

# Maxfiy kalitlar
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv(
    'ALLOWED_HOSTS',
    'localhost,127.0.0.1,chustfeelfood.netlify.app,chustfeelfood.onrender.com,chustfeelfoodbackend.onrender.com'
).split(',')

# Ilovalar
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',  # Sizning app nomingiz
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL va WSGI
ROOT_URLCONF = 'feelfood.urls'

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

WSGI_APPLICATION = 'feelfood.wsgi.application'

# Ma'lumotlar bazasi
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}

# Xalqaro vaqt va til
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik va media fayllar
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.getenv('RENDER_MEDIA_ROOT', BASE_DIR / 'media')

# CORS (frontenddan kirish uchun ruxsat)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',  # Vite
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://chustfeelfood.netlify.app',
    'https://chustfeelfood.onrender.com',
    'https://chustfeelfoodbackend.onrender.com',
]
CORS_ALLOW_CREDENTIALS = True

# CSRF uchun trusted originlar
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'https://chustfeelfood.netlify.app',
    'https://chustfeelfood.onrender.com',
    'https://chustfeelfoodbackend.onrender.com',
]

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],  
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ],
}

# Maxfiy kalitlar (.env dan olinadi)
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
