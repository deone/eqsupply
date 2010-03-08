
import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import account.views
import quote.views

urlpatterns = patterns('',
    url(r'^$', account.views.login, name="acct_login"),
    url(r'^signup$', account.views.signup, name="acct_signup"),
    url(r'^activate', account.views.activate, name="acct_activate"),
    url(r'^logout$', account.views.logout, name="acct_logout"),
    (r'^user/(?P<user_id>\d+)/item_count$', account.views.count_line_items),

    (r'^products$', include('products.urls')),
    (r'^products/', include('products.urls')),

    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
