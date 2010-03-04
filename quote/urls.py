from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",
    (r'^(?P<product_id>\d+)/quote$', views.add_line_item),
)
