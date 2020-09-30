from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

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
