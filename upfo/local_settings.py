DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'upfo.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

STATIC_ROOT = '/Users/rvrseppala/Development/Byy/By/upfo/media/'

STATIC_URL = 'media/'

FACEBOOK_APP_ID = '200047203426040'
FACEBOOK_API_SECRET = 'efbddb138180cb38af95785c866f9b5d'

ADMIN_MEDIA_PREFIX = '/static/admin/'