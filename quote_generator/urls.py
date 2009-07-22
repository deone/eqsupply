from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {"template": "quote_generator/index.html"}, name="products_home"),
)
