from .common import *

import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['9dc001240c2442698429c68b17ed665e.vfs.cloud9.us-east-1.amazonaws.com']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ['HTTP_X_FORWARDED_PHOTO', 'https']

