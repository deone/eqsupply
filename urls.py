
import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import account.views


urlpatterns = patterns('',
    url(r'^$', account.views.login, name="acct_login"),
    url(r'^signup$', account.views.signup, name="acct_signup"),
    url(r'^activate', account.views.activate, name="acct_activate"),
    url(r'^logout$', 'django.contrib.auth.views.logout', {"template_name": "account/login.html"}, name="acct_logout"),

    (r'products$', include('product.urls')),

    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
