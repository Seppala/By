import os
# Django settings for upfo project.

DEBUG = True

ADMINS = (
    ('Riku', 'riku@seppa.la'),
)

MANAGERS = ADMINS
if DEBUG == True:
	
	DATABASES = {
	'default': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	'NAME': 'upfo_dev',                      # Or path to database file if using sqlite3.
	'USER': 'upfoR',                      # Not used with sqlite3.
	'PASSWORD': '',                  # Not used with sqlite3.
	'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
	'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
	}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'


#Adding paths
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates')
    
)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = '/Users/rvrseppala/Development/Byy/by/upfo/media/'
#MEDIA_ROOT = '/Users/rikuseppala/Development/upfo/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (        os.path.join(SITE_ROOT, 'static'),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=kr#ino$hxeq!by%57!_19hlyqd+7jcg5uad6xhbn7i97eirku'

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
)

ROOT_URLCONF = 'upfo.urls'

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
    'django.contrib.admindocs',
    'south',
    'upfoMain',
	'social_auth',
	'jsonhandler',
	'facebookapi',
	'fbtestusers',
	'storages',
	'gunicorn',
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

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'django.contrib.auth.backends.ModelBackend',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
	'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_type_backends',
	'upfoMain.context_processors.app_id',
)
	
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook',)

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

FACEBOOK_APP_ID = '336824476371187'
FACEBOOK_API_SECRET = 'cd506a8e3991e98dd7f9f089b7cc0473'
TWITTER_CONSUMER_KEY			  = ''
TWITTER_CONSUMER_SECRET			  = ''
#FACEBOOK_APP_ID					  = '126197457491070'
#FACEBOOK_APP_SECRET				  = '2ed91326e1a7c88db7358727856877dc'
LINKEDIN_CONSUMER_KEY			  = ''
LINKEDIN_CONSUMER_SECRET		  = ''
ORKUT_CONSUMER_KEY				  = ''
ORKUT_CONSUMER_SECRET			  = ''
GOOGLE_OAUTH2_CLIENT_ID			  = ''
GOOGLE_OAUTH2_CLIENT_SECRET		  = ''
SOCIAL_AUTH_CREATE_USERS		  = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME	  = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME	  = 'socialauth_complete'
LOGIN_ERROR_URL					  = '/login/error/'
#SOCIAL_AUTH_USER_MODEL			   = 'upfoMain.CustomUser'
SOCIAL_AUTH_ERROR_KEY			  = 'socialauth_error'
GITHUB_APP_ID					  = ''
GITHUB_API_SECRET				  = ''
FOURSQUARE_CONSUMER_KEY			  = ''
FOURSQUARE_CONSUMER_SECRET		  = ''

AUTH_PROFILE_MODULE = 'upfoMain.CustomUser'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
AWS_ACCESS_KEY_ID = 'AKIAIC3ODO5IXDRKAMVQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'by_static'
STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

try:
    from local_settings import *
except ImportError:
    pass