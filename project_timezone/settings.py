"""
Django settings for project_timezone project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
# from decouple import config
# from storages.backends.s3boto3 import S3Boto3Storage


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-r$_mhe7@!7p=(gdv@j^kx)+00%u7tfdfede9=8wol&%@j^t0!r'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', cast=bool) #using bool function convert DEBUG to boolean
DEBUG = True

# ALLOWED_HOSTS = ['timezone.up.railway.app', '127.0.0:1']


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smartwatches',
    'category',
    'accounts',
    'adminpannel',
    'store',
    'carts',
    'orders',
    'wishlists',
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
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'project_timezone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
                'wishlists.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_timezone.wsgi.application'
AUTH_USER_MODEL = 'accounts.Account'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Render postersql database

import dj_database_url



DATABASES = {

    'default': dj_database_url.parse('postgres://timezonedatabase_user:66McmXyw6nBlF0QIqFvxF6KwQaLKpPp6@dpg-cgokg0orddl9mmrtu5e0-a.ohio-postgres.render.com/timezonedatabase')
            
}

# DATABASES = {
#     'default': {    
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test2',
#         'USER': 'postgres',
#         'PASSWORD': 'amjad12345',
        
        
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': config('ENGINE'),
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'HOST': config('HOST'),
#         'PORT': config('DATABASE_PORT', cast=int),
#     }
# }

  

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
# MEDIA_URLS ='/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS=[BASE_DIR/ 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}




# SMTP configuration
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'amjadchatholi@gmail.com'
# EMAIL_HOST_PASSWORD = 'rkytulqsavlmedvv'
# EMAIL_USE_TLS = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'amnasanu100@gmail.com'
EMAIL_HOST_PASSWORD = 'utquoihfalxixyun'
EMAIL_PORT = 587

# EMAIL_BACKEND = config('EMAIL_BACKEND')                                     
# EMAIL_HOST = config('EMAIL_HOST', default='localhost') 
# EMAIL_PORT =  config('EMAIL_PORT', cast=int)     
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')     
# EMAIL_HOST_PASSWORD =  config('EMAIL_HOST_PASSWORD')       
# EMAIL_USE_TLS =   config('EMAIL_USE_TLS', cast=bool)  

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:8000",
#     "https://timezone.up.railway.app",
# ]
# CSRF_TRUSTED_ORIGINS = [
#     "http://127.0.0.1:8000",
#     "https://timezone.up.railway.app",
#     ]


# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# AWS_ACCESS_KEY_ID = 'AKIAUHMTEUDU4IUGD6MA'


# AWS_SECRET_ACCESS_KEY = '4/hNH/J5NMqQ5eect26H7O8ojI91+Q3vfqNz/Gqo'

# AWS_QUERYSTRING_AUTH = False

# AWS_STORAGE_BUCKET_NAME = 'newtimezone-bucket'

# AWS_S3_FILE_OVERWRITE = True

