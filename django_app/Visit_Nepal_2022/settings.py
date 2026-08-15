"""
Django settings for Visit_Nepal_2022 project.

For more information on this file, see:
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Base directory — two levels up from this file (django_app/)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Security
# SECURITY WARNING: keep the secret key used in production secret!
# In production, load this from an environment variable, e.g.:
#   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
# ---------------------------------------------------------------------------
SECRET_KEY = 'mcd!%mzre0u$k0s%^yeg)=znkbksvh%55cwm&1*n9mcqhlhk*('

# SECURITY WARNING: never run with DEBUG=True in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# ---------------------------------------------------------------------------
# Application definition
# ---------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project apps
    'pages_content',
    'login_register',
    'members',
    'pages',
    'chatbot',
    'hotel_management_system',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Visit_Nepal_2022.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'login_register' / 'template',
            BASE_DIR / 'members' / 'template',
            BASE_DIR / 'pages' / 'template',
            BASE_DIR / 'hotel_management_system' / 'template',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Visit_Nepal_2022.wsgi.application'


# ---------------------------------------------------------------------------
# Database — SQLite for development
# ---------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ---------------------------------------------------------------------------
# Password validation
# ---------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ---------------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ---------------------------------------------------------------------------
# Static & Media files
# ---------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'   # used by collectstatic in production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ---------------------------------------------------------------------------
# Auth redirects
# ---------------------------------------------------------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/members'
LOGOUT_REDIRECT_URL = '/explore'


# ---------------------------------------------------------------------------
# Default primary key field type (silences Django 3.2+ warning)
# ---------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
