import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('BONAPETITE_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bpmodels.apps.BpmodelsConfig',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
        ('rest_framework.permissions.IsAuthenticated', ),
    'PAGE_SIZE': 10
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bonapetite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bpmodels/templates/bpmodels'),
                 os.path.join(BASE_DIR, 'bpmodels/templates/layouts'),
                 os.path.join(BASE_DIR, 'bpmodels/templates/registration'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'bonapetite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
path_url = os.environ.get('BONAPETITE_DATABASE_URL')
db_from_env = dj_database_url.config(default=path_url, conn_max_age=500)
DATABASES = {'default': {}}
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
password_validation = 'django.contrib.auth.password_validation.'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': password_validation+'UserAttributeSimilarityValidator', },
    {'NAME': password_validation+'MinimumLengthValidator', },
    {'NAME': password_validation+'CommonPasswordValidator', },
    {'NAME': password_validation+'NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/'
