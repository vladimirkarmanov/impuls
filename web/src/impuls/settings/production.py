from .base import *

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'register.apps.RegisterConfig',
    'events.apps.EventsConfig',
    'documents.apps.DocumentsConfig'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'connection.cnf'),
        }
    }
}

# Media and statifiles
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True
