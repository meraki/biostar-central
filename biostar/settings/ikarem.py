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

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'biostar',
    },
}

NAVBAR_TAGS = []

POST_TAG_LIST = NAVBAR_TAGS

SOCIALACCOUNT_PROVIDERS = {}

if get_env("PRODUCTION_MODE") == "true":
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_HOST_USER = 'biostar'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'ask-no-reply@meraki.com'

CAPTCHA = False
