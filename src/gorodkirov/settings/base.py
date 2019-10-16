import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party apps
    'mptt',
    'captcha',
    'easy_thumbnails',
    'widget_tweaks',
    'debug_toolbar',

    # social account
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.instagram',

    'gorodkirov.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'gorodkirov.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'gorodkirov.wsgi.application'

AUTH_PASSWORD_VALIDATORS = []

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'

USE_I18N = True

USE_L10N = True

USE_TZ = False

MEDIA_ROOT = os.path.join(BASE_DIR, '../../public_html/media/')
STATIC_ROOT = os.path.join(BASE_DIR, '../../public_html/static/')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, 'photo_contest/static'),
    # os.path.join(BASE_DIR, 'projects/static/projects'),
    # os.path.join(BASE_DIR, 'wiki/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# reCaptcha v2
RECAPTCHA_PUBLIC_KEY = '6Lfbhr0UAAAAAEq58JSa3iLcr76uedRuEl5C8SpY'
RECAPTCHA_PRIVATE_KEY = '6Lfbhr0UAAAAAFyiFQARIV9kU6x4FaVqWT2C7PE-'
RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000'}


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

