from django.conf.urls.defaults import *

import views
import quote.views

urlpatterns = patterns("",
    url(r'^$', views.index, name="product_home"),
    (r'^(?P<product_id>\d+)$', views.display_product),
    (r'^(?P<product_id>\d+)/quote$', quote.views.add_line_item),
)
