"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib import messages
from datetime import timedelta
from django.utils.functional import LazyObject, empty
from dotenv import load_dotenv
from pathlib import Path
import environ
import dj_database_url



import os
from storages.backends.s3boto3 import S3Boto3Storage

# Set the AWS S3 custom storage class for static files
class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = 'staticfiles'


# Set the AWS S3 custom storage class for media files (no specific location)
class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = ''


DEFAULT_APP_URL = os.getenv('DEFAULT_APP_URL')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR,".env") )

ONLY_ADMIN = os.getenv('ONLY_ADMIN', 'off') == 'on'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "1234")

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG") != "False"

#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATICFILES_DIR = os.path.join(BASE_DIR, "staticfiles")

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "media")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
ONLY_ADMIN = os.getenv('ONLY_ADMIN', 'off') == 'on'
#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_CREDENTIALS = True
#CORS_ALLOW_ALL_ORIGINS = True 


AWS_ACCESS_KEY_ID= os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME= os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME= os.getenv('AWS_S3_REGION_NAME')

class MyTokenObtainPairViewLazy(LazyObject):
    def _setup(self):
        from accounts.views import MyTokenObtainPairView
        self._wrapped = MyTokenObtainPairView()

MyTokenObtainPairView = MyTokenObtainPairViewLazy


# Application definition

INSTALLED_APPS = [
    'admin_volt.apps.AdminVoltConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    

    'rest_swagger',
    'storages',
    
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "drf_yasg",
    "accounts",
    'rest_framework',
    'rest_framework_swagger',
    'djoser',
    'sotp',
    'django_apscheduler',
    'physical_storage',
    'digital',
    
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'core.urls'

#authentication
DJOSER = {
    'SEND_ACTIVATION_EMAIL': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': False,
    'ACTIVATION_URL':'auth/activation/{uid}/{token}', #change to Frontend url
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password-reset/{uid}/{token}', #change to Frontend url
    'LOGOUT_ON_PASSWORD_CHANGE': False,
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.UserCreateSerializer',
        'current_user': 'accounts.serializers.UserSerializer',
    },
    'EMAIL':{
     'password_reset':'accounts.views.PasswordResetEmail'
    }
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', 'Bearer'),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,

    # use the custom token serializer
    'TOKEN_SERIALIZER': MyTokenObtainPairView,

    # add the custom claims to the token
    'CLAIMS': {
        'name': 'auth.name',
        'role': 'auth.role',
        'email': 'auth.email',
        'is_staff': 'auth.is_staff',
        'username' : 'auth.username'
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#database_url = os.environ.get('DATABASE_URL')




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# CORS HEADERS


CORS_ALLOWED_ORIGINS= os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')

CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# settings.py
CORS_ALLOW_ALL_ORIGINS = True  # This allows all origins during development.



# For production, specify the allowed origins explicitly:
# CORS_ALLOW_ALL_ORIGINS = False
# CORS_ALLOWED_ORIGINS = [
#     "https://example-am-a.onrender.com",
#     # Add other allowed origins as needed.
# ]

CORS_ALLOW_CREDENTIALS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'auth/login/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 	#MEDIA_DIR
FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520





# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rest Routes Configuration
OTP_LENGTH = 6

# Register User model in admin
REGISTER_USER_MODEL = True

# SOTP Defintion
SOTP_TIME_EXPIRATION = 5
SOTP_FROM_EMAIL = "noreply@email.com"

AUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },]

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}



LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTH_USER_MODEL = 'accounts.user'  #'app.User'
DEFAULT_FILE_STORAGE = 'core.settings.MediaRootS3Boto3Storage'
STATICFILES_STORAGE = 'core.settings.StaticRootS3Boto3Storage'
#STATICFILES_LOCATION = 'staticfiles'

#AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/staticfiles/'



AWS_LOCATION = 'staticfiles'
STATICFILES_LOCATION = AWS_LOCATION
