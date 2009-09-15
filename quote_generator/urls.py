from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "quote_generator/index.html"}, name="quote_generator_index"),
    url(r'^create_or_edit/$', views.quote_home, name="create_edit_quote"),

    # These url mappings've been rendered useless!
    url(r'^manufacturers/$', direct_to_template, {"template": "quote_generator/manufacturers.html"}, name="manufacturers"),
    url(r'^categories/$', direct_to_template, {"template": "quote_generator/categories.html"}, name="categories"),
    (r'^manufacturer_list/$', views.view_products_by, {"view": "manufacturer"}),
    (r'^category_list/$', views.view_products_by, {"view": "category"}),
    (r'^manufacturer/(?P<manufacturer_id>\d+)/$', views.products),
    (r'^category/(?P<category_id>\d+)/$', views.products),
    (r'^setquote/$', views.quote, {"action": "set"}),
    (r'^unsetquote/$', views.quote, {"action": "unset"}),
)
