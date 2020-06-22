from .base import *

DEBUG = True

SECRET_KEY = '&%%-%z_s*$fj%(^(^0&%5%9!&5%5!0!65%*%VJ!^(^05-_3f&!$a$&u5&&&!'

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
    'documents.apps.DocumentsConfig',
    'chats.apps.ChatsConfig'
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
