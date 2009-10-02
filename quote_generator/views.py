from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext
from django.http import HttpResponse
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
    user_account = UserAccount.objects.get(pk=user_id)

    return render_to_response(template, {
	"user_account": user_account
    }, context_instance=RequestContext(request))

@h.json_response
def create_quote(request):
    user_id = request.POST.get("user").strip()
    company = request.POST.get("company").strip()

    user = User.objects.get(pk=user_id)
    user_account = UserAccount.objects.get(pk=user_id)
    time_created = datetime.datetime.now()
    # Ideally, this should be a setting, it shouldn't be hardcoded.
    title = company.title() + " Quote, " + str(time_created)

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
	products = Product.objects.filter(categories=category_id)
	result_set = make_result_set(quote_id, category_id, "category", products, Category)
    else:
	products = Product.objects.filter(manufacturer=manufacturer_id)
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
	QuoteItem.objects.create(quote=quote, product=product, quantity=quantity, quote_item_cost=0)

	return ("ok", "Product Added")

    if action == "unset":
	QuoteItem.objects.filter(quote=quote, product=product).delete()
	return ("ok", "Product Removed")

def product_groups(request, template="quote_generator/product_home.html"):
    quote_id = request.GET.get("quote_id").strip()
    quote = Quote.objects.get(pk=quote_id)
    
    return render_to_response(template, {
	"quote": quote
    }, context_instance=RequestContext(request))

def preview_quote(request, quote_id, template="quote_generator/quote_preview.html"):
    # Quote action links should be made dumb if status=1
    quote = Quote.objects.get(pk=quote_id)

    return render_to_response(template, {
	"quote": quote
    }, context_instance=RequestContext(request))

@h.json_response
def email(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    user_id = request.POST.get("user_id").strip()
    email = User.objects.get(pk=user_id).email

    subject, from_email, to = "YOUR QUOTE, %s" % quote.title, "noreply@aerixnigeria.com", email
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
