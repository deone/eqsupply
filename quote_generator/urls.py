from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "quote_generator/index.html"}, name="quote_generator_index"),
    url(r'^home/$', direct_to_template, {"template": "quote_generator/quote.html"}, name="quote_home"),
    (r'^create/$', views.create_quote),
    url(r'^(?P<quote_id>\d+)/view_categories/$', direct_to_template, {"template": "quote_generator/product_home.html"}, name="product_home"),
    url(r'^manufacturers/$', direct_to_template, {"template": "quote_generator/manufacturers.html"}, name="manufacturers"),
    (r'^manufacturer_list/$', views.view_products_by, {"view": "manufacturer"}),
    url(r'^categories/$', direct_to_template, {"template": "quote_generator/categories.html"}, name="categories"),
    (r'^category_list/$', views.view_products_by, {"view": "category"}),


    # These url mappings've been rendered useless!
    (r'^manufacturer/(?P<manufacturer_id>\d+)/$', views.products),
    (r'^category/(?P<category_id>\d+)/$', views.products),
    (r'^setquote/$', views.quote, {"action": "set"}),
    (r'^unsetquote/$', views.quote, {"action": "unset"}),
)
