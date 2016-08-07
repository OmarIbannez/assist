from config.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOU NEED A SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'assist',
        'USER': 'assist',
        'PASSWORD': 'assist',
        'HOST': 'localhost',
        'PORT': '',
    }
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
