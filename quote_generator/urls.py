from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="products_home"),
    url(r'^manufacturers/$', direct_to_template, {"template": "quote_generator/manufacturers.html"}, name="manufacturers"),
    url(r'^categories/$', direct_to_template, {"template": "quote_generator/categories.html"}, name="categories"),
    (r'^manufacturer_list/$', views.view_products_by, {"view": "manufacturer"}),
    (r'^category_list/$', views.view_products_by, {"view": "category"}),
    (r'^manufacturer/(?P<manufacturer_id>\d+)/$', views.products),
    (r'^category/(?P<category_id>\d+)/$', views.products),
    (r'^setquote/$', views.quote, {"action": "set"}),
    (r'^unsetquote/$', views.quote, {"action": "unset"}),
)
