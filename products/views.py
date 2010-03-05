from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from products.models import *
from quote.forms import LineItemForm

from eqsupply import helpers as h

APP_MENU = Division.objects.all()

def index(request, template="products/index.html"):
    categories = Category.objects.all()
    
    return render_to_response(template, {
	"menu": APP_MENU,
	"categories": categories,
    }, context_instance=RequestContext(request))

def display_product(request, product_id, form_class=LineItemForm, template="products/product.html"):
    product = get_object_or_404(Product, pk=product_id)
    form = form_class()

    return render_to_response(template, {
	"menu": APP_MENU,
	"product": product,
	"form": form,
    }, context_instance=RequestContext(request))
