# Django settings for webnotes project.

import os
DIRNAME = os.path.dirname(__file__)

TIME_FORMAT = 'H-i-s'
DATE_FORMAT = 'Y-F-j'# This is used by the SelectDateWidget in django.forms.extras.widgets http://stackoverflow.com/a/6137099/412329
DATETIME_FORMAT = 'Y-F-j H-i-s' 
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True # https://docs.djangoproject.com/en/dev/topics/cache/#the-per-site-cache


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Rome'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-uk'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False # needed to set this to false to get SelectDateWidget in django.forms.extras.widgets to work http://stackoverflow.com/a/6137099/412329

MEDIA_ROOT = os.path.join(DIRNAME, 'uploads')
MEDIA_URL = 'http://127.0.0.1/media/'
STATIC_ROOT = os.path.join(DIRNAME, 'static')
STATIC_URL = 'http://127.0.0.1/static/'

# ln -s ~/django_projects/notes-env/lib/python2.6/site-packages/django/contrib/admin/media/ ~/django_projects/notes-env/webnotes/static/admin
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/static/",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
    # 'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'webnotes.middleware.LoginFormMiddleware', # required to have login form on every page - http://stackoverflow.com/questions/2734055/putting-a-django-login-form-on-every-page
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    # display django version in footer using template tag defined in context_processors.py - http://stackoverflow.com/questions/4256145/django-template-tag-to-display-django-version
    'webnotes.context_processors.django_version',
    # required to have login form on every page and for templatetags - http://stackoverflow.com/questions/2734055/putting-a-django-login-form-on-every-page
    'django.core.context_processors.request',
)
 
TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates')
)

ROOT_URLCONF = 'webnotes.urls'

# URL of the login page.
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/notes/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # enabling markup so we can have markdown. requires http://www.freewisdom.org/projects/python-markdown
    'django.contrib.markup',
    # pretty punctuation - http://code.google.com/p/typogrify/
    'typogrify',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'notes',
    'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# database, secret key, etc are in settings_local.py
try:
    from settings_local import *
except ImportError:
    pass