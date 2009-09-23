from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "quote_generator/index.html"}, name="quote_generator_index"),
    url(r'^home/$', direct_to_template, {"template": "quote_generator/quote.html"}, name="quote_home"),
    url(r'^manufacturers/$', direct_to_template, {"template": "quote_generator/manufacturers.html"}, name="manufacturers"),
    url(r'^categories/$', direct_to_template, {"template": "quote_generator/categories.html"}, name="categories"),

    (r'^(?P<quote_id>\d+)/preview/$', views.preview_quote),
    (r'^(?P<quote_id>\d+)/email/$', views.email),
    (r'^create/$', views.create_quote),
    (r'^(?P<quote_id>\d+)/add_product/$', views.product_list),
    (r'^set_quote_item/$', views.quote_item, {"action": "set"}),
    (r'^unset_quote_item/$', views.quote_item, {"action": "unset"}),
)
