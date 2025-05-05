from pathlib import Path
import os
from dotenv import load_dotenv

# Bazaviy papka yo'lini aniqlash
BASE_DIR = Path(__file__).resolve().parent.parent

# .env fayldan ma'lumotlarni yuklash
load_dotenv(BASE_DIR / '.env')

# Muhit o'zgaruvchilari
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Ruxsat etilgan hostlar
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,chustfeelfood.netlify.app,chustfeelfood.onrender.com,chustfeelfoodbackend.onrender.com').split(',')

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
    'api',  # sizning app nomingiz
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # bu yuqorida bo'lishi kerak!
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Xalqaro sozlamalar
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik fayllar
STATIC_URL = '/static/'

# Media fayllar (agar rasm yuklansa)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CORS sozlamalari
CORS_ALLOWED_ORIGINS = [
    'https://chustfeelfood.netlify.app',
    'https://chustfeelfood.onrender.com',
    'https://chustfeelfoodbackend.onrender.com',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
CORS_ALLOW_CREDENTIALS = True

# CSRF trusted originlar (POST request uchun)
CSRF_TRUSTED_ORIGINS = [
    'https://chustfeelfood.netlify.app',
    'https://chustfeelfood.onrender.com',
    'https://chustfeelfoodbackend.onrender.com',
    'http://localhost:5173',  
]

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Stripe va Telegram sozlamalari
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
