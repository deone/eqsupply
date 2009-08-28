from django.shortcuts import render_to_response
from django.template import RequestContext
from quote_generator.models import Manufacturer
from django.core.serializers import serialize

from eqsupply import helpers as h

@h.json_response
def index(request, template="quote_generator/index.html"):
    
    return render_to_response(template, {
    }, context_instance=RequestContext(request))

@h.json_response
def manufacturers(request):
    manufacturer_list = Manufacturer.objects.all()
    json = serialize("json", manufacturer_list)

    return ("ok", json)
