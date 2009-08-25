from django.shortcuts import render_to_response
from django.template import RequestContext

def options(request, template="quote_generator/index.html"):
    return render_to_response(template, {
    }, context_instance=RequestContext(request))
