from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.core.serializers import serialize
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext
from django.http import HttpResponse
from django.http import Http404
from django.conf import settings

from django.contrib.auth.models import User
from account.models import UserAccount

from eqsupply import helpers as h
from quote_generator.models import *

import datetime
from traceback import print_exc

@h.json_response
def quote_home(request, template="quote_generator/quote.html"):
    user_id = request.GET.get("user_id").strip()
    user_account = get_object_or_404(UserAccount, pk=user_id)

    return render_to_response(template, {
	"user_account": user_account
    }, context_instance=RequestContext(request))

@h.json_response
def create_quote(request):
    user_id = request.POST.get("user").strip()
    company = request.POST.get("company").strip()

    user = get_object_or_404(User, pk=user_id)
    time_created = datetime.datetime.now()
    # Ideally, this should be a setting, it shouldn't be hardcoded.
    title = "Equipment Quote For " + company.title()

    quote = Quote.objects.create(user=user, title=title, quote_cost=0, time_created=time_created, status=False)

    return ("ok", quote.todict())

def view_products_by(request, view):
    list_model_map = {"manufacturer": Manufacturer, "category": Category}

    list = list_model_map[view].objects.all()
    json = serialize("json", list)

    return HttpResponse(json, mimetype="application/json")

def product_list(request, quote_id, template="quote_generator/products.html"):
    manufacturer_id = request.GET.get("manufacturer_id")

    if manufacturer_id == None:
	category_id = request.GET.get("category_id")
	products = get_list_or_404(Product, categories=category_id)
	result_set = make_result_set(quote_id, category_id, "category", products, Category)
    else:
	products = get_list_or_404(Product, manufacturer=manufacturer_id)
	result_set = make_result_set(quote_id, manufacturer_id, "manufacturer", products, Manufacturer)

    return render_to_response(template, {"result": result_set}, context_instance=RequestContext(request))

def make_result_set(quote_id, type_id, type, product_list, model):
    return  {
		"quote": quote_id,
		type: model.objects.get(pk=type_id), 
		"products": product_list,
		"product_index": settings.ELCOMETER_PRODUCTS_INDEX,
		"specs_index": settings.ELCOMETER_SPECS_INDEX
	    }

@h.json_response
def quote_item(request, action):
    quote_id = request.POST.get("quote").strip()
    product_id = request.POST.get("product").strip()
    
    quote = Quote.objects.get(pk=quote_id)
    product = Product.objects.get(pk=product_id)

    if action == "set":
	quantity = request.POST.get("quantity").strip()

	if int(quantity) == 0:
	    return ("error", "Quantity cannot be zero")

	try:
	    product_exist = get_object_or_404(QuoteItem, quote=quote, product=product)
	    product_exist.quantity = int(product_exist.quantity) + int(quantity)
	    product_exist.save()
	except Http404:
	    QuoteItem.objects.create(quote=quote, product=product, quantity=quantity, quote_item_cost=0)

	return ("ok", "Product Added")

    if action == "unset":
	get_object_or_404(QuoteItem, quote=quote, product=product).delete()
	return ("ok", "Product Removed")

def product_groups(request, template="quote_generator/product_home.html"):
    quote_id = request.GET.get("quote_id").strip()
    quote = get_object_or_404(Quote, pk=quote_id)
    
    return render_to_response(template, {
	"quote": quote
    }, context_instance=RequestContext(request))

DAYS_OF_WEEK = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

AFTERNOON = {
    13: 1,
    14: 2,
    15: 3,
    16: 4,
    17: 5,
    18: 6,
    19: 7,
    20: 8,
    21: 9,
    22: 10,
    23: 11,
    24: 12,
}

def convert_date(date):
    return DAYS_OF_WEEK[date.isoweekday()] + " " + MONTHS[date.month] + " " + str(date.day) + ", " + str(date.year)

def convert_time(time):
    time_split = time.split(":")
    hour = int(time_split[0])
    minutes = time_split[1]
    
    if hour > 12:
	hour_12 = AFTERNOON[hour]
	return str(hour_12) + ":" + minutes + "pm"
    else:
	return str(hour) + ":" + minutes + "am"

def preview_quote(request, quote_id, template="quote_generator/quote_preview.html"):
    quote = get_object_or_404(Quote, pk=quote_id, status=0)
    if not quote.quoteitem_set.all():
	raise Http404

    readable_date = convert_date(quote.time_created)

    time = str(quote.time_created.time())
    readable_time = convert_time(time)

    quote.time_created = readable_date + " at " + readable_time

    return render_to_response(template, {
	"quote": quote
    }, context_instance=RequestContext(request))

@h.json_response
def count_quote_items(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    try:
	quote_items = get_list_or_404(QuoteItem, quote=quote)
	return ("ok", len(quote_items))
    except Http404:
	return ("ok", 0)

@h.json_response
def email(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    user_id = request.POST.get("user_id").strip()
    email = get_object_or_404(User, pk=user_id).email

    subject, from_email, to = quote.title, "noreply@aerixnigeria.com", email
    text_content = ""
    html_content = create_email(quote)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    quote.status = 1
    quote.save()

    return ("ok", "Quote Sent")

def create_email(quote):
    html = "<html>"
    html += """
	    <body style="background-color: #FFF; margin: 0; color: #333; font-family: Arial, sans-serif; font-size: 10pt;">
	    """
    html += "<h1 style='margin:0px; font-size:160%'>" + quote.title + "</h1>"
    html += "<p>Created " + str(quote.time_created) + "</p>"
    html += """
	    <table width="100%" style="border-spacing: 0px">
		<thead>
		    <tr>
			<th style="border-top: solid 1px #ddd; border-bottom: solid 1px #ddd; text-align: left; width: 62.5%; line-height: 2em; text-align: left; padding-left: 10px; margin: 0px;>
			    <h3 style="margin: 0">Item</h3>
			</th>

			<th style="border-top: solid 1px #ddd; border-bottom: solid 1px #ddd; text-align: left; line-height: 2em; padding-left: 10px; margin: 0px;>
			    <h3 style="margin: 0">Manufacturer</h3>
			</th>

			<th style="border-top: solid 1px #ddd; border-bottom: solid 1px #ddd; text-align: left; line-height: 2em; padding-left: 10px; margin: 0px;>
			    <h3 style="margin: 0">Quantity</h3>
			</th>
		    </tr>
		</thead>
		<tbody>
	    """
    for qi in quote.quoteitem_set.all():
	html += """<tr>
		    <td style="padding-left: 10px; margin: 0px; border-bottom: solid 1px #ddd; vertical-align: top;">
			<h4 style="margin: 0; font-size: 110%; margin: 5px 0px 5px 0px;">""" + qi.product.name + """</h4>
		    </td>
		    <td style="padding-left: 10px; margin: 0px; border-bottom: solid 1px #ddd; vertical-align: top;">
			<p style="padding-top:5px; margin: 0px 0px 5px 0px;">""" + qi.product.manufacturer.name + """</p>
		    </td>
		    <td style="padding-left: 10px; margin: 0px; border-bottom: solid 1px #ddd; vertical-align: top;">
			<p style="padding-top:5px; margin: 0px 0px 5px 0px;">""" + str(qi.quantity) + """</p>
		    </td>
		</tr>
		"""
    html += "</tbody></table>"
    html += "</body></html>"

    return html
