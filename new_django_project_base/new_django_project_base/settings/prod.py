from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Unique production key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


RUNNING_ENVIRONMENT='production'


INSTALLED_APPS += [
]


STATIC_ROOT = os.path.join(BASE_DIR,'static/')
STATIC_URL = '/static/'

