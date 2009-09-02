from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.template import RequestContext
from django.http import HttpResponse

from eqsupply import helpers as h
from quote_generator.models import Manufacturer, Category

def view_products_by(request, view):
    list_model_map = {"manufacturer": Manufacturer, "category": Category}

    list = list_model_map[view].objects.all()
    json = serialize("json", list)

    return HttpResponse(json, mimetype="application/json")

def products(request, manufacturer_id=None, category_id=None):
    """if manufacturer_id:
	print manufacturer_id
    else:
	print category_id"""
    
