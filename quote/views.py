from reportlab.pdfgen import canvas
from django.http import HttpResponse, Http404

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from eqsupply.account.models import Account
from eqsupply.quote.forms import *
from eqsupply.quote.models import *
from eqsupply.products.models import Division
from eqsupply.cost.models import *
from eqsupply import helpers as h
from eqsupply import settings

APP_MENU = Division.objects.all()

@login_required
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

def get_user_account(user_id):
    user = get_object_or_404(User, pk=user_id)
    user_account = get_object_or_404(Account, user=user)

    return user_account

#@login_required
def fetch_quote(request, quotation_id, form_class=UserDetailCheckForm, template="quote/quotation.html", **kwargs):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    quotation.VAT = settings.VAT/100.0 * int(quotation.cost)

    form = form_class()

    line_item_list = list(quotation.lineitem_set.all())

    i = 0

    user_account = get_user_account(quotation.user.id)

    while i < int(quotation.lineitem_set.count()):
	line_item_list[i].id = i + 1
	i = i + 1

    return render_to_response(template, {
	"menu": APP_MENU,
	"quotation": quotation,
	"line_items": line_item_list,
	"user_account": user_account,
	"user_detail_form": form,
    }, context_instance=RequestContext(request))

def process_quote(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    sub_total = quotation.cost

    vat = settings.VAT/100.0 * int(quotation.cost)

    # Logistics
    user = get_object_or_404(User, pk=quotation.user.id)
    user_account = get_object_or_404(Account, user=user)

    #Int'l courier charge
    #...

    #Local courier charge
    local_courier_charge = compute_local_courier_charge(user_account.location, quotation.lineitem_set.all())

    # Compute line_item courier charge with each line_item's weight and user location, add up all.
    # Compute courier VAT & 20% markup to cater for custom charges et al.
    # Compute courier insurance

def compute_local_courier_charge(location_id, line_items):
    courier_charge = 0
    zone = get_object_or_404(Location, pk=location_id).zone

    for l in line_items:
	try:
	    weight = get_object_or_404(Weight, weight=l.product.weight)
	except Http404:
	    weight = get_object_or_404(Weight, weight=round(l.product.weight))
	
	cost = get_object_or_404(Cost, weight=weight, zone=zone)
	courier_charge = courier_charge + cost.cost

    return courier_charge
