from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from products.models import ProductVariation
from quote.models import *

from eqsupply import helpers as h

import datetime

def prefix_zero(number):
    if number < 10:
	return "0" + str(number)

def generate_quote_no():
    today = datetime.datetime.now()
    no_of_quotes_this_month = Quotation.objects.filter(time_created__month=today.month).count()

    quote_no = "AGS "
    quote_no += prefix_zero(today.month) + "-"
    quote_no += str(today.year)[2:4] + "-"
    quote_no += prefix_zero(no_of_quotes_this_month + 1)

    return quote_no

@h.json_response
def add_line_item(request, product_id, **kwargs):
    user_id = request.POST.get("user")
    user = get_object_or_404(User, pk=user_id)

    try:
	"""
	All quotes are processed end-to-end such that a user cannot create
	a new quote if he hasn't either closed or discarded the current one.
	This is to ensure that we have at most 1 open quote per user. KISS!
	"""
	quotation = get_object_or_404(Quotation, user=user, status=0)
    except Http404:
	quotation = Quotation.objects.create(user=user, time_created=datetime.datetime.now(), \
		quotation_no=generate_quote_no(), cost=0, status=False)

    product = get_object_or_404(ProductVariation, pk=product_id)
    quantity = request.POST.get("quantity")

    line_item = LineItem.objects.create(quotation=quotation, product=product, quantity=quantity, cost=product.cost)

    return ("ok", "Item Added")
