from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

from eqsupply.quote.forms import LineItemForm
from eqsupply.quote.models import *
from eqsupply.products.models import Division
from eqsupply import helpers as h

APP_MENU = Division.objects.all()

@h.json_response
def add_line_item(request, prod_var_id, form_class=LineItemForm, **kwargs):
    form = form_class(request.POST)

    if form.is_valid():
	line_item = form.save(prod_var_id)
	# Do we have to replicate account/views/line_item_quantity return value here too?
	result = {
	    "id": line_item.quotation.id,
	    "date_created": h.format_date(str(line_item.quotation.time_created.date())),
	    "line_item_qty": line_item.quotation.lineitem_set.all().count()
	}
	return ("object", result)

    return h.dict_error(form.errors.items())

def fetch_quote(request, quotation_id, template="quote/quotation.html"):
    quotation = get_object_or_404(Quotation, pk=quotation_id)

    return render_to_response(template, {
	"menu": APP_MENU,
	"quotation": quotation,
    }, context_instance=RequestContext(request))
