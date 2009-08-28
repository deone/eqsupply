from django.conf.urls.defaults import *
from django.conf import settings

import quote_generator.views

from django.contrib import admin
admin.autodiscover()

import os

urlpatterns = patterns('',
    (r'^$', include('account.urls')),
    (r'^account/', include('account.urls')),
    (r'^products/', include('quote_generator.urls')),
    (r'^manufacturers/', quote_generator.views.manufacturers),
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
