from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'rawdatatech',
        'USER': 'postgres',
        'PASSWORD': 'abcd1234',
        'OPTIONS': {
            # "autocommit": True,
        },
    }
}



BASE_URL = "http://app.com/"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rdtcontacttree@gmail.com'
EMAIL_HOST_PASSWORD = 'invincible123#$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
