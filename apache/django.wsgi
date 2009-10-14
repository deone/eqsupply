import os
import sys
import django.core.handlers.wsgi

sys.stdout = sys.stderr

sys.path.append("/usr/local/www")
sys.path.append("/usr/local/www/eqsupply")

os.environ["DJANGO_SETTINGS_MODULE"] = "eqsupply.settings_production"

application = django.core.handlers.wsgi.WSGIHandler()
