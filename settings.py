# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os


if os.path.abspath(os.path.dirname(__file__)) == '/Users/andy/Sites/potato':
  ENVIRONMENT = 'development'
  GOOGLELOADERKEY = 'ABQIAAAAmHuhDSBEw1ehYJgA4v432RT2yXp_ZAY8_ufC3CFXhHIE1NvwkxRfQsTXJt7aKwRQtHE4cj2sjt_JkA'

elif os.path.abspath(os.path.dirname(__file__)) == 'somestagingpath':
  ENVIRONMENT = 'staging'
  GOOGLELOADERKEY = 'TBC'

else:
  ENVIRONMENT = 'production'
  GOOGLELOADERKEY = 'ABQIAAAAmHuhDSBEw1ehYJgA4v432RRnlEyiPxHiLjMS5smxw7QIAsiTHhT2hknFkQ9zd5tD9xPKcDOCgu9Yuw'


# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'gae'}
DATABASES['gae'] = {'ENGINE': 'djangoappengine.db'}

AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = 'TYUImksdcjknkdYGKJKBHVGHNJJVHYUVWDNWJFonerfneonefd'

OAUTH_APP_SETTINGS = {}

OAUTH_APP_SETTINGS['twitter'] = {
    'consumer_key': 'bua0zIvvU8iRKYCL8R823Q',
    'consumer_secret': 'o7fG99m200b9twicDhGQmeRjkiG3tRlimRtXfxlrBY',
    'request_token_url': 'https://twitter.com/oauth/request_token',
    'access_token_url': 'https://twitter.com/oauth/access_token',
    'user_auth_url': 'http://twitter.com/oauth/authorize',
    'default_api_prefix': 'http://twitter.com',
    'default_api_suffix': '.json',
    'access_token': '371287992-U3atxDyCJ65Oz2XVpjiVy8z6zCRnPoHWkIjyjKNy',
    'access_token_secret': '7bAj2ydG3HltJy4I2N7m3TEb5X7iBrys44Ep5W30vQ',
}

INSTALLED_APPS = (
#    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'registration',
    'txm',
    'twitter',
    'oauth2',
)

# djangoappengine should come last, so it can override a few manage.py commands
INSTALLED_APPS += ('djangoappengine',)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

#TEMPLATE_CONTEXT_PROCESSORS = default_settings.TEMPLATE_CONTEXT_PROCESSORS + (
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    "django.core.context_processors.i18n",
    'django.core.context_processors.media',
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    'txm.context_processors.api_keys',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

