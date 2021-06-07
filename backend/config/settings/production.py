import environ

from .base import *

env = environ.Env()
env.read_env(env_file='.env')

DEBUG = False

SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT')
    }
}
