"""
Django settings for RestroBE project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

from django.contrib.messages import constants as messages
from .emailsetting import SET_EMAIL_USE_TLS, SET_EMAIL_HOST, SET_EMAIL_HOST_USER, \
    SET_EMAIL_HOST_PASSWORD, SET_EMAIL_PORT, SET_EMAIL_BACKEND, SET_DEFAULT_FROM_EMAIL


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(q2p54npn&!#cs$opj)hfl%a57x6kt&a67868-b$i6l=(n@(fj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminapp',
    'userapp',
    'mainapp',
    'restaurentapp',
    'storages',
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

ROOT_URLCONF = 'RestroBE.urls'

TEMPLATES = [
   {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'assets/templates')],
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

WSGI_APPLICATION = 'RestroBE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'Restro',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD':'',
        'PORT':'3306',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# #AWS S3

# AWS_ACCESS_KEY_ID = 'AKIA47QNQMANLQJVYR4L'

# AWS_SECRET_ACCESS_KEY = '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'

# AWS_STORAGE_BUCKET_NAME = 'nannapravalikas3bucket'

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# AWS_DEFAULT_ACL = 'public-read'

# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400'
# }

# AWS_LOCATION = 'static'

# AWS_QUERYSTRING_AUTH = False

# AWS_HEADERS = {
#     'Access-Control-Allow-Origin': '*'
# }

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# #STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'assets/static'),]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

#EMAIL SETTING
EMAIL_USE_TLS = SET_EMAIL_USE_TLS
EMAIL_HOST = SET_EMAIL_HOST
EMAIL_HOST_USER = SET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SET_EMAIL_HOST_PASSWORD
EMAIL_PORT = SET_EMAIL_PORT
EMAIL_BACKEND = SET_EMAIL_BACKEND
DEFAULT_FROM_EMAIL = SET_DEFAULT_FROM_EMAIL 