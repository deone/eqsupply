from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import quote_generator.views

import os

urlpatterns = patterns('',
    (r'^$', include('account.urls')),
    (r'^account/', include('account.urls')),
    (r'^quote/', include('quote_generator.urls')),
    (r'^product_groups/', quote_generator.views.product_groups),
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
