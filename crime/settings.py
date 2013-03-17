import os
import django

# CHASE NOTE: These are a few settings that I put into EVERY SINGLE DJANGO PROJECT that I build. You don't
# need to know how they work; the only thing you need to know is that they will make your life INFINITELY
# EASIER. In fact, I would recommend copying them into your new projects when you start work on them after
# the break (don't forget the two imports above).

DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PROJECT_NAME = 'crime'

# These two settings (normally found further down in the document) can cause very obnoxious problems depending
# on how your computer is set up. Setting them up like this (using the helpful settings tools above) avoids those
# problems and allows things to just magically work. If you copy these into your new project settings files, be
# sure to DELETE THE ONES DJANGO PLACES IN THE SETTINGS FILE BY DEFAULT. THERE SHOULD ONLY BE ONE STATIC_ROOT AND
# TEMPLATE_DIRS SETTING IN YOUR SETTINGS FILE -- AND IT SHOULD BE THESE (rant over).

STATIC_ROOT = os.path.join(SITE_ROOT, '%s/static' % PROJECT_NAME)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, '%s/templates' % PROJECT_NAME)
)

########## NORMAL DJANGO SETTINGS BEGIN HERE ###########

# Django settings for crime project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# CHASE NOTE: Remember, we care about the DATABASES setting. For development purposes, just set the engine
# to sqlite3 as below and give your database a name. That's all you need to do!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'crime.sqlite',                      # Or path to database file if using sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w$$apzca&q!2&*ewhd6&n)74c#4=^=ccc2jq0h1ybs==phy*qe'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crime.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crime.wsgi.application'

# CHASE NOTE: Remember, we also care about the INSTALLED_APPS setting. Two important things to
# keep in mind here: One, uncomment the lines as noted to enable the admin (if you want it). And two:
# ANY APP YOU CREATE AND WANT TO USE MUST BE ADDED TO THIS LIST. Note the 'crime.data' string below.

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    'crime.data',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
