import os
import sys
sys.path.append("/usr/local/www")
sys.path.append("/usr/local/www/eqsupply")
os.environ["DJANGO_SETTINGS_MODULE"] = "eqsupply.settings_production"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()