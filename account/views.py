from traceback import print_exc

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from django.template import RequestContext
from django.conf import settings

from account.forms import SignupForm, LoginForm
from quote_generator.models import Quote

from account.models import Account

from eqsupply import helpers as h

def dict_error(errors):
    error_dict = {}
    keys = []

    for k, v in errors:
	error_dict[k] = str(v)
	keys.append(k)

    error_dict["keys"] = keys

    return ("error", error_dict)

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
		return ("ok", "Signup Successful")
	    except Exception, e:
		user.delete()
		print_exc()
		return ("conn_error", "Unable to reach eqsupply. Check your internet connection and try again.")

        return dict_error(form.errors.items())

    else:
        form = SignupForm()

        return render_to_response(template, {
            "form": form,
        }, context_instance=RequestContext(request))

@h.json_response
def login(request, form_class=LoginForm, template="account/login.html", **kwargs):
    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            form.login(request)
            return ("ok", "Login Successful")

        errors = dict_error(form.errors.items())

        return dict_error(form.errors.items())
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
    request.flash['feedback'] = "Your account is now active. Please log in to proceed."

    form = form_class()

    return render_to_response(template, {
	"form": form,
    }, context_instance=RequestContext(request))

@h.json_response
def add_details(request, user_id, **kwargs):
    user = get_object_or_404(Account, pk=user_id)

    user.phone = request.POST.get("phone").strip()
    user.company = request.POST.get("company").strip()
    user.position = request.POST.get("position").strip()
    user.company_street_address = request.POST.get("company_address").strip()
    user.city = request.POST.get("city").strip()
    user.state = request.POST.get("state").strip()
    user.country = request.POST.get("country").strip()
    user.save()

    quote_id = request.POST.get("quote_id").strip()
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.title = quote.title + user.company
    quote.save()

    return ("ok", "Details Added")

@h.json_response
def has_details(request, user_id, **kwargs):
    user = get_object_or_404(Account, pk=user_id)
    if not user.company:
	return ("error", "No details")
    else:
	return ("ok", "Details Available")

@h.json_response
def get_company(request, user_id, **kwargs):
    user_account = get_object_or_404(Account, pk=user_id)
    user_company = user_account.company

    return ("ok", user_company)
