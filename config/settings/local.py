from .base import *


# Secret Settings

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = ['django_gulp'] + INSTALLED_APPS

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]


# Other

INTERNAL_IPS = ["127.0.0.1", ]


# Gulp

GULP_CWD = "'{}'".format(os.path.join(BASE_DIR, 'static'))
GULP_DEVELOP_COMMAND = 'gulp --cwd {}'.format(GULP_CWD)
GULP_PRODUCTION_COMMAND = 'gulp build --cwd {}'.format(GULP_CWD)


# Cors Headers
CORS_ORIGIN_REGEX_WHITELIST = [
    'http:\/\/localhost:.*'
]
