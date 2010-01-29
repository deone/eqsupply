from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from products.models import Category

from eqsupply import helpers as h

def index(request, template="products/index.html"):
    categories = Category.objects.all()
    
    return render_to_response(template, {
	"categories": categories
    }, context_instance=RequestContext(request))
