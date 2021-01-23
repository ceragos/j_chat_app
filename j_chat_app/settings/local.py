from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'j_chat_app',
        'USER': 'postgres',
        'PASSWORD': 'abril2017',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
