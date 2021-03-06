import os, sys
PROJECT_DIR = os.path.dirname(__file__)
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        # Don't do this. It dramatically slows down the test.
#        'NAME': '/tmp/chroniker.db',
#        'TEST_NAME': '/tmp/chroniker.db',
    }
}
ROOT_URLCONF = 'chroniker.tests.urls'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'chroniker',
    'chroniker.tests',
]
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
SOUTH_TESTS_MIGRATE = False
USE_TZ = True

AUTH_USER_MODEL = 'auth.User'

SECRET_KEY = 'abc123'

SITE_ID = 1

BASE_SECURE_URL = 'https://localhost'
BASE_URL = 'http://localhost'
