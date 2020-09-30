from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloud_storage',
        'USER': 'root',
        'PASSWORD': 'Zomper',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
