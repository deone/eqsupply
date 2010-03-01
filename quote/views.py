from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from quote.models import *

from eqsupply import helpers as h

@h.json_response
def add_line_item(request, product_id, **kwargs):
    return ("ok", "Item Added")
