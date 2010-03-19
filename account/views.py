from traceback import print_exc

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from django.template import RequestContext
from django.conf import settings
from django.http import Http404

from account.models import Account
from account.forms import SignupForm, LoginForm
from quote.models import Quotation

from eqsupply import helpers as h

@h.json_response
def signup(request, form_class=SignupForm, template="account/signup.html", **kwargs):
    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            user = form.save()
	    reg_id = user.account_set.get(user=user.id).reg_id
	    try:
		user.email_user("Aerix Equipment Supply Account Activation", "Click this link to activate your account: %s" % create_activation_link(reg_id), settings.EMAIL_SENDER)
		request.flash['feedback'] = "Thank you for registering. An activation link has been sent to your email."
		return (True, "Signup Successful")
	    except Exception, e:
		user.delete()
		print_exc()
		return ("conn_error", "Unable to reach eqsupply. Check your internet connection and try again.")

        return h.dict_error(form.errors.items())

    else:
        form = form_class()

        return render_to_response(template, {
            "form": form,
        }, context_instance=RequestContext(request))

@h.json_response
def login(request, form_class=LoginForm, template="account/login.html", **kwargs):
    if request.method == "POST":
    
	default_redirect_to = "/products"
	redirect_to = request.REQUEST.get("next")

	if not redirect_to or "://" in redirect_to or " " in redirect_to:
            redirect_to = default_redirect_to

        form = form_class(request.POST)

        if form.login(request):
            return (True, redirect_to)

        return h.dict_error(form.errors.items())

    else:
        form = form_class()

        return render_to_response(template, {
            "form": form, 
        }, context_instance=RequestContext(request))

def logout(request, form_class=LoginForm, template="account/login.html"):
    request.session.flush()
    request.flash['feedback'] = "You are now logged out."
    

    form = form_class()

    return render_to_response(template, {
	"form": form,
    }, context_instance=RequestContext(request))

def create_activation_link(reg_id):
    url = settings.BASE_URL + "activate?reg_id=%s" % reg_id
    return url

def activate(request, form_class=LoginForm, template="account/login.html"):
    reg_id = request.GET['reg_id']
    user_id = get_object_or_404(Account, reg_id=reg_id).user_id
    user = get_object_or_404(User, id=user_id)
    user.is_active = 1
    user.save()
    request.flash['feedback'] = "Your account is now active. You may log in now."

    form = form_class()

    return render_to_response(template, {
	"form": form,
    }, context_instance=RequestContext(request))

@h.json_response
def line_item_quantity(request, user_id, **kwargs):
    user = get_object_or_404(User, pk=user_id)

    try:
	quotation = get_object_or_404(Quotation, user=user, status=0)
	result = {
	    "id": quotation.id,
	    "date_created": h.format_date(str(quotation.time_created.date())),
	    "line_item_qty": quotation.lineitem_set.all().count()
	}
	return ("object", result)
    except Http404:
	return ("object", {"line_item_qty": 0, "date_created": None})
