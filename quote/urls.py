from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",
    (r'^(?P<quotation_id>\d+)$', views.fetch_quote),
    (r'^(?P<quotation_id>\d+)/process$', views.process_quote),
)
