"""
Django settings for project_repo project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from pathlib import Path
import json

from django.core.exceptions import ImproperlyConfigured

PROJECT_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = Path(PROJECT_DIR).resolve(strict=True).parent
APPLICATION_DIR = Path(BASE_DIR).resolve(strict=True).parent

with open(APPLICATION_DIR / 'secrets.json') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.
    Thanks to twoscoopsofdjango'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY = get_secret('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'blog.apps.BlogConfig',
    #'accounting.apps.AccountingConfig',
    #'portfolio.apps.PortfolioConfig',
    #'streamblocks',
    #'streamfield',
    'captcha',
    'taggit',
    'crispy_forms',
    'treebeard',
    'private_storage',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'project.processors.get_global_settings',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly', ],
}

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

TAGGIT_CASE_INSENSITIVE = True

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
    'wide_landscape': {'verbose_name': 'Orizzontale', 'width': 1600, 'height': 800, 'opts': 'crop'},
    'landscape': {'verbose_name': 'Orizzontale', 'width': 1280, 'height': 720, 'opts': 'crop'},
    'portrait': {'verbose_name': 'Verticale', 'width': 768, 'height': 1024, 'opts': 'crop'},
    'square': {'verbose_name': 'Quadrato', 'width': 768, 'height': 768, 'opts': 'crop'},
    }

FETCH_EMAILS = True

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LANGUAGE_CODE = get_secret('LANGUAGE_CODE')#'en-us'

TIME_ZONE = get_secret('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'
PROFILE_IS_TRUSTED_BY_DEFAULT = False

RECAPTCHA_TEST_MODE = False

#this is for the accounting email receiver module
IMAP_HOST = get_secret('IMAP_HOST')
IMAP_USER = get_secret('IMAP_USER')
IMAP_PWD = get_secret('IMAP_PWD')
IMAP_PORT = get_secret('IMAP_PORT')
IMAP_FROM = get_secret('IMAP_FROM')

#This stuff has nothing to do with django.site
WEBSITE_NAME = get_secret('WEBSITE_NAME')
WEBSITE_ACRO = get_secret('WEBSITE_ACRO')
#footer external links
#make your own, add them in project.processors.get_global_settings
FB_LINK = get_secret('FB_LINK')
INSTA_LINK = get_secret('INSTA_LINK')
TWIT_LINK = get_secret('TWIT_LINK')
IN_LINK = get_secret('IN_LINK')
GITHUB_LINK = get_secret('GITHUB_LINK')
EXT_LINK = get_secret('EXT_LINK')
