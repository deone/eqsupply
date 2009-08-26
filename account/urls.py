from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^$', views.login, name="acct_login"),
	url(r'^signup/$', views.signup, name="acct_signup"),
	url(r'^activate/', views.activate, name="acct_activate")
)
