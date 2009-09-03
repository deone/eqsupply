from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.template import RequestContext
from django.http import HttpResponse

from eqsupply import helpers as h
from quote_generator.models import Manufacturer, Category, Product

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
		"products": product_list
	    }
