from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth.models import User
from quote_generator.forms import QuoteForm

from eqsupply import helpers as h
from quote_generator.models import *

import datetime

def quote_home(request, template="quote_generator/quote.html"):
    # return pending user quotes to template (if any)
    return render_to_response(template, {}, context_instance=RequestContext(request))

def get_pending_quote():
    pass

@h.json_response
def create_quote(request):
    user_id = request.POST.get("user").strip()
    title = request.POST.get("title").strip()

    user = User.objects.get(pk=user_id)
    time_created = datetime.datetime.now()

    Quote.objects.create(user=user, title=title, quote_cost=0, time_created=time_created, status=False)

    return ("ok", "Quote Created")

def view_products_by(request, view):
    list_model_map = {"manufacturer": Manufacturer, "category": Category}

    list = list_model_map[view].objects.all()
    json = serialize("json", list)

    return HttpResponse(json, mimetype="application/json")

def products(request, template="quote_generator/products.html", manufacturer_id=None, category_id=None):
    if manufacturer_id:
	products = Product.objects.filter(manufacturer=manufacturer_id)
	result_set = make_result_set(manufacturer_id, "manufacturer", products, Manufacturer)

    if category_id:
	products = Product.objects.filter(categories=category_id)
	result_set = make_result_set(category_id, "category", products, Category)

    return render_to_response(template, {"result": result_set}, context_instance=RequestContext(request))

def make_result_set(type_id, type, product_list, model):
    return  {
		type: model.objects.get(pk=type_id), 
		"products": product_list,
		"product_index": settings.ELCOMETER_PRODUCTS_INDEX,
		"specs_index": settings.ELCOMETER_SPECS_INDEX
	    }

@h.json_response
def quote(request, action):
    user_id = request.POST.get("user").strip()
    product_id = request.POST.get("product").strip()
    
    user = User.objects.get(pk=user_id)
    product = Product.objects.get(pk=product_id)

    if action == "set":
	quantity = request.POST.get("quantity").strip()
	Quote.objects.create(user=user, product=product, quantity=quantity)

	return ("ok", "Product Added")

    if action == "unset":
	Quote.objects.filter(user=user, product=product).delete()
	return ("ok", "Product Removed")
