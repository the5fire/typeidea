# flake8: noqa

from .base import *  # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [
     'silk.middleware.SilkyMiddleware',
]
