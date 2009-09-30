from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^$', views.login, name="acct_login"),
    url(r'^signup/$', views.signup, name="acct_signup"),
    url(r'^activate/', views.activate, name="acct_activate"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {"template_name": "account/logout.html"}, name="acct_logout"),
    (r'^(?P<user_id>\d+)/pending_quotes/$', views.get_pending_quotes),
)
