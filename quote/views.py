from django.template import RequestContext
from django.contrib.auth.models import User

from quote.forms import LineItemForm
from quote.models import *

from eqsupply import helpers as h

@h.json_response
def add_line_item(request, prod_var_id, form_class=LineItemForm, **kwargs):
    form = form_class(request.POST)

    if form.is_valid():
	line_item = form.save(prod_var_id)
	return ("ok", "Item Added")

    return h.dict_error(form.errors.items())
