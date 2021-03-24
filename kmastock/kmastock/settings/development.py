"""
Django settings for kmastock project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

########## PATH CONFIGURATION
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__))) # represents BASE_DIR

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qo2_v4smxtsu06p9kb1^v3u8cv-au+b@l5iz*)l!6yn_*6^5=6'
#config('SECRET_KEY')#
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new

    # Third party app
    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new'django.contrib.sites', # new
    'crispy_forms',
    'bootstrap',
    'bootstrap4',
    'django_tables2',
    'jquery',
    'phonenumber_field',
    'widget_tweaks', 

    # My apps
    'apps.accounts',
    'apps.barcodes',
    'apps.category',
    'apps.clients',
    'apps.clientsaccts',
    'apps.home',
    'apps.products',
    'apps.returns',
    'apps.sales',
    'apps.search',
    'apps.stocks',
    'apps.vendors',
    'apps.vendorsaccts',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# for django-allauth manage users login,signup and logout 
AUTH_USER_MODEL = 'accounts.CustomUser' # new

LOGIN_REDIRECT_URL = '/' # means frontpage
ACCOUNT_LOGOUT_REDIRECT_URL = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # new for translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'kmastock.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT, 'templates')],
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

WSGI_APPLICATION = 'kmastock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # for postgresql database
        # 'ENGINE': 'django.db.backends.postgresql',#config('DATABASE_ENGINE'),#
        # 'NAME': 'kmadb',#config('DATABASE_NAME'),  # Name of the database itself
        # 'USER': 'postgres',#config('DATABASE_USER'),
        # 'PASSWORD':#config('DATABASE_PASSWORD'),
        # 'HOST': 'localhost',#config('DATABASE_HOST'),
        # 'PORT': '5432',#config('DATABASE_PORT'), #'5432',
        ################################################
        'ENGINE': os.environ.get('DATABASE_ENGINE'), #config('DATABASE_ENGINE'),
        'NAME': os.environ.get('KMADB'),#config('KMADB'),# Name of the database itself
        'USER': os.environ.get('DATABASE_USER'),# config('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),##config('DATABASE_PASSWORD'),#
        'HOST': os.environ.get('DATABASE_HOST'),#config('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),#config('DATABASE_PORT'), #'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static_root') #(BASE_DIR, '../static_root') 
print('STATIC_ROOT= '+str(STATIC_ROOT))
STATICFILES_DIRS =[
    os.path.join(SITE_ROOT, 'static')##(BASE_DIR, '../static') # important to do '../static' instead of 'static'
]
print('STATICFILES_DIRS= '+str(STATICFILES_DIRS))

from django.utils.translation import gettext_lazy as _

LOCALE_PATHS = [
   os.path.join(SITE_ROOT, 'locale'),
   os.path.join(SITE_ROOT, "apps/home/locale"),
]
#print(BASE_DIR,STATIC_URL,LOCALE_PATHS,STATIC_ROOT,os.path.join(SITE_ROOT, "templates"))
LANGUAGES = (
    ('ar', _('Arabic')),
    ('en', _('English')),
    ('de', _('German')),
)

MULTILINGUAL_LANGUAGES = (
    "en",
    "ar",
    'de',
)

print('DJANGO_ROOT= '+str(DJANGO_ROOT))
print('SITE_ROOT= '+str(SITE_ROOT))
print('SITE_NAME= '+str(SITE_NAME))
print('Append= '+str(path.append(DJANGO_ROOT)))

# for authentication by email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = False # True
ACCOUNT_USERNAME_REQUIRED = True # False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True # False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'#'email'
ACCOUNT_UNIQUE_EMAIL = True