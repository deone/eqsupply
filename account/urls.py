from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'account.views.login', name="acct_login"),
)
