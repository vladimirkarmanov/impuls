import environ

from .base import *

env = environ.Env()
env.read_env(env_file='dev.env')

DEBUG = True

SECRET_KEY = env.str('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'register.apps.RegisterConfig',
    'events.apps.EventsConfig',
    'documents.apps.DocumentsConfig'
]

MIDDLEWARE += [
    'livereload.middleware.LiveReloadScript'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
