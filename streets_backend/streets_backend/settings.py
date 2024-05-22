# Django 5.0.6
import os

from datetime import timedelta
from dotenv import load_dotenv
from pathlib import Path

<<<<<<< HEAD
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'infra', '.env')
load_dotenv(dotenv_path)

=======
load_dotenv()
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)
BASE_DIR = Path(__file__).resolve().parent.parent

BASE_URL = os.getenv('BASE_URL')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = bool(os.getenv('DEBUG', default=False))

EMPTY_VALUE: str = '-пусто-'

<<<<<<< HEAD
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
=======
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
<<<<<<< HEAD
    'rest_framework.authtoken',
    'myauth.apps.MyauthConfig',
=======
    'rest_framework_simplejwt',
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)
    'contacts.apps.ContactsConfig',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'events.apps.EventsConfig',
    'streetculture.apps.StreetCultureConfig',
    'aboutus.apps.AboutusConfig',
    'drf_yasg',
    'djoser',
    'django_filters'
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

ROOT_URLCONF = 'streets_backend.urls'

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

WSGI_APPLICATION = 'streets_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
<<<<<<< HEAD
        'rest_framework.authentication.TokenAuthentication',
=======
        'rest_framework_simplejwt.authentication.JWTAuthentication',
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
<<<<<<< HEAD
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    ),
=======
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)
    'PAGE_SIZE': 5,

}

<<<<<<< HEAD
=======
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)
AUTH_USER_MODEL = 'users.CustomUser'
