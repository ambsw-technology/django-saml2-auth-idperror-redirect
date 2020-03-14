import os
from os.path import dirname, abspath

DEBUG = True
TEMPLATE_DEBUG = True

TIME_ZONE = 'America/New_York'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_saml2_auth',
    'django_saml2_auth_idperror_redirect',
    'testproject',
)

ROOT_URLCONF = 'testproject.urls'

SECRET_KEY = '9q7324#45RWtw843q$%&/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3'),
    }
}

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

SAML2_AUTH = {
    'DEFAULT_NEXT_URL': '/',
    'ENTITY_ID': 'https://test.example.com',
    'ASSERTION_URL': 'https://test.example.com',
    'PLUGINS': {
        'IDP_ERROR': ['REDIRECT'],
    },
    'METADATA_LOCAL_FILE_PATH': os.path.join(DJANGO_ROOT, 'saml.xml'),
    'ATTRIBUTES_MAP': {'username': 'Email'},
    # test cases need to work long after the sample payloads expire
    'ACCEPTED_TIME_DIFF': 999999999,
}
