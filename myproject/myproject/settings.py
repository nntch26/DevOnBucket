"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y1s=g&po*pc-1=0(cdar0#t(iv344#mlr3evfe#dzj4+5p(e9='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['98.84.126.215:8000']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',  
    'myapp',
    'ckeditor',
    'ckeditor_uploader'

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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'myproject.wsgi.application'
CRISPY_TEMPLATE_PACK = "bootstrap5"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "blogs_db",
#         "USER": "postgres",
#         "PASSWORD": "1234",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blogs_db",
        "USER": "postgres",
        "PASSWORD": "e6J5vqefbdCMiU8",
        "HOST": "database-1.ctlz1iab3j2z.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

import os
from pathlib import Path


# CKEditor settings
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"

CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': '100%', 
        'extraPlugins': ','.join([
            'codesnippet',
            'image2',
            'font',
        ]),
        'toolbar_Custom': [
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},  # เพิ่มปุ่ม Font และ FontSize
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar']},
        ],
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
