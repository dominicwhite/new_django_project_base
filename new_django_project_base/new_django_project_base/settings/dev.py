from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'GenerateRandomKeyHere'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

RUNNING_ENVIRONMENT = 'development'


INSTALLED_APPS += [
]


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
