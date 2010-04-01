from django.shortcuts import get_object_or_404
from django import forms
from django.http import Http404
from django.contrib.auth.models import User

from products.models import ProductVariant
from quote.models import *

import datetime

class LineItemForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput())
    user = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
	if self._errors:
	    return
	if self.cleaned_data["quantity"] < 1:
	    raise forms.ValidationError("Invalid Quantity")

	return self.cleaned_data

    def save(self, prod_var_id):
	quantity = self.cleaned_data["quantity"]
	user = get_object_or_404(User, pk=self.cleaned_data["user"])

	try:
	    quotation = get_object_or_404(Quotation, user=user, status=0)
	except Http404:
	    quotation = Quotation.objects.create(user=user, time_created=datetime.datetime.now(), \
		    quotation_no=generate_quote_no(), cost=0, status=False)

	product = get_object_or_404(ProductVariant, pk=prod_var_id)

	try:
	    """ If line item already exists """
	    line_item = get_object_or_404(LineItem, product=product, quotation=quotation)
	    line_item.quantity += quantity  # update quantity
	    line_item.cost = str(float(line_item.cost) + float(product.cost) * int(quantity))	# update cost
	    line_item.save()
	    
	except Http404:
	    """ If line item doesn't exist, just create a new one """
	    line_item = LineItem.objects.create(quotation=quotation, product=product, quantity=quantity, \
		    cost_per_unit=product.cost, cost=str(float(product.cost) * int(quantity)))

	quotation.cost = str(float(quotation.cost) + float(line_item.cost))
	quotation.save()

	return line_item

class UserDetailCheckForm(forms.Form):
    company = forms.CharField(widget=forms.HiddenInput())

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
