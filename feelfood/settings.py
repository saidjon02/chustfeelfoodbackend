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

# ALLOWED_HOSTS - vergul bilan ajratilgan string => list ga aylantiriladi
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Django ilovalari
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payme',
    'rest_framework',
    'api',
]

# Middleware lar
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

# URL
ROOT_URLCONF = 'feelfood.urls'

# Templates
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

# WSGI
WSGI_APPLICATION = 'feelfood.wsgi.application'

# Baza: SQLite (hozircha)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Til va vaqt
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik fayllar
STATIC_URL = '/static/'

# Modellar uchun default primary key turi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS (Netlify yoki frontend bilan ishlashi uchun)
CORS_ALLOW_ALL_ORIGINS = True

# Stripe va Telegram
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
BOT_TOKEN        = os.getenv('BOT_TOKEN')
CHAT_ID          = os.getenv('CHAT_ID')
CSRF_TRUSTED_ORIGINS = [
    'https://chustfeelfood.onrender.com',  # Sizning frontend manzilingiz
]