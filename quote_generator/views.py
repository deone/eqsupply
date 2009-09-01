from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.http import HttpResponse

from eqsupply import helpers as h
from quote_generator.models import Manufacturer

def manufacturer_list(request):
    manufacturer_list = Manufacturer.objects.all()
    json = serialize("json", manufacturer_list)

    return HttpResponse(json, mimetype="application/json")
