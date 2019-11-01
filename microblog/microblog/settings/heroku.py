from .common import *

import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES['default']=dj_database_url.config() 

SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')


