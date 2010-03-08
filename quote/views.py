from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.contrib.auth.models import User

from quote.forms import LineItemForm
from quote.models import *

from eqsupply import helpers as h

@h.json_response
def add_line_item(request, prod_var_id, form_class=LineItemForm, **kwargs):
    form = form_class(request.POST)

    if form.is_valid():
	line_item = form.save(prod_var_id)
	return ("object", line_item.quotation.line_item_qty())

    return h.dict_error(form.errors.items())
