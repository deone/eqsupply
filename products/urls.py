from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",
    url(r'^$', views.index, name="product_home"),
    (r'^(?P<product_id>\d+)$', views.display_product),
)
