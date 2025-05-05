# settings.py
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
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,localhost:8000,chustfeelfood.netlify.app,chustfeelfood.onrender.com,chustfeelfoodbackend.onrender.com').split(',')

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
    'corsheaders.middleware.CorsMiddleware',
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

# Ma'lumotlar bazasi (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Xalqaro sozlamalar\LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik fayllar
STATIC_URL = '/static/'

# CORS sozlamalari
CORS_ALLOWED_ORIGINS = [
    'https://chustfeelfood.netlify.app',
    'https://chustfeelfood.onrender.com',
    'https://chustfeelfoodbackend.onrender.com',
    'http://localhost',
    'http://127.0.0.1',
    'http://localhost:8000',
]
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'https://chustfeelfood.netlify.app',
    'https://chustfeelfood.onrender.com',
    'https://chustfeelfoodbackend.onrender.com',
]

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Stripe va Telegram
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


# ----------------------------------------------------------------------
# api/models.py
from django.db import models
from django.contrib.postgres.fields import JSONField

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    items = JSONField()  # taomlar ro'yxatini JSON da saqlaydi
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.name}"


# ----------------------------------------------------------------------
# api/serializers.py
from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'items', 'subtotal', 'delivery_fee', 'total', 'created_at']
