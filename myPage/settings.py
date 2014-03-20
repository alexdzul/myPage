import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'ei*s1wng!+^7y639(@gkv&17%@2a0ow&5x9a7s10%#)syb+(wq'


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myPage.apps.main',
    'myPage.apps.social',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myPage.urls'

WSGI_APPLICATION = 'myPage.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'my_data.db'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'myPage/media')


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'myPage/static'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'myPage/templates'),
)