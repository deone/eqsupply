# Django settings for eqsupply project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Oladayo Osikoya', 'alwaysdeone@gmail.com'),
    ('Obinna Eneh', 'obinna@aerixnigeria.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'eqsupply'             # Or path to database file if using sqlite3.
DATABASE_USER = 'eqadmin'             # Not used with sqlite3.
DATABASE_PASSWORD = 'eqadmin'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Lagos'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'u#grkf32ey!ju-fp#cr%8$lw^_eo*lwqclfx%dob9n9va4oddh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "djangoflash.middleware.FlashMiddleware",
)

ROOT_URLCONF = 'eqsupply.urls'

import os.path

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'eqsupply.account',
    'eqsupply.products',
    'eqsupply.quote',
)

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
#EMAIL_HOST_USER = "erecruit"
#EMAIL_HOST_PASSWORD = "3r3cru17"

CACHE_BACKEND = "locmem:///"

SESSION_ENGINE = "django.contrib.sessions.backends.cache"


TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request",
	"djangoflash.context_processors.flash",
)

FLASH_STORAGE = "session"

BASE_URL = "http://localhost:7700/"

ACTIVATION_EMAIL_SUBJECT = "Your Registration: AERIX EQUIPMENT SUPPLY"

EMAIL_SENDER = "dayo@aerixnigeria.com"

ACTIVATION_EMAIL_MESSAGE = "This is your activation link:\n\n%s" 

TEST_DATABASE_CHARSET = "latin1"

TEST_DATABASE_COLLATION = "latin1_swedish_ci"

ELCOMETER_PRODUCTS_INDEX = "http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/"
ELCOMETER_SPECS_INDEX = "http://www.elcometer.com/international index pages/international/product pages - English/product pages/technical specifications/"

LOGIN_URL = "/"
