from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^(?P<user_id>\d+)/company/$', views.get_company),
    (r'^(?P<user_id>\d+)/add_details/$', views.add_details),
    (r'^(?P<user_id>\d+)/has_details/$', views.has_details),
)
