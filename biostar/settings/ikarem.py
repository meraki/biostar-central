# -*- coding: utf8 -*-
#
# Ikarem settings
#
from .base import *

# If you comment out the DB settings, the default DB settings from base.py will be used.
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env('DATABASE_NAME'),
        'USER': 'biostar',
        'PASSWORD': get_env('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': 5432,
     }
}
