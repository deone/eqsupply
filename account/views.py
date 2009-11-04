from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from django.template import RequestContext
from django.conf import settings

from account.forms import SignupForm, LoginForm
from account.models import UserAccount
from quote_generator.models import Quote

from eqsupply import helpers as h

def dict_error(errors):
    error_dict = {}
    keys = []

    for k, v in errors:
        error_dict[k] = v
        keys.append(k)

    if keys != ["__all__"]:
        error_dict["keys"] = keys

    return error_dict

@h.json_response
def get_company(request, user_id, **kwargs):
    user_account = get_object_or_404(UserAccount, pk=user_id)
    user_company = user_account.company

    return ("ok", user_company)

@h.json_response
def login(request, form_class=LoginForm, template="account/login.html", **kwargs):
    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            form.login(request)
            return ("ok", "Login Successful")

        errors = dict_error(form.errors.items())

        return ("error", errors)
    else:
        form = form_class()

        return render_to_response(template, {
            "form": form, 
        }, context_instance=RequestContext(request))

@h.json_response
def signup(request, form_class=SignupForm, template="account/signup.html", **kwargs):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            email, reg_id = form.save()
            email_user(email, reg_id)
            request.flash['feedback'] = "Registration successful. An activation email has been sent to %s." % email
            return ("ok", "Signup Successful")

        errors = dict_error(form.errors.items())

        return("error", errors)
    else:
        form = SignupForm()

        return render_to_response(template, {
            "form": form,
        }, context_instance=RequestContext(request))

def email_user(email, reg_id):
    activation_link = create_activation_link(reg_id)
    email_list = []
    email_list.append(email)
    subject = settings.ACTIVATION_EMAIL_SUBJECT
    message = settings.ACTIVATION_EMAIL_MESSAGE % activation_link
    sender = settings.EMAIL_SENDER

    send_mail(subject, message, sender, email_list, fail_silently=False)

def create_activation_link(reg_id):
    url = settings.BASE_URL + "account/activate/?reg_id=%s" % reg_id
    return url

def activate(request):
    reg_id = request.GET['reg_id']
    activated_user = get_object_or_404(UserAccount, reg_id=reg_id)
    activated_user.is_active = 1
    activated_user.save()
    #request.flash['feedback'] = "Registration successful. An activation email has been sent to %s." % email

    return render_to_response("account/activate.html", {
	"user": activated_user,
    }, context_instance=RequestContext(request))

@h.json_response
def add_details(request, user_id, **kwargs):
    user = get_object_or_404(UserAccount, pk=user_id)

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
    user = get_object_or_404(UserAccount, pk=user_id)
    if not user.company:
	return ("error", "No details")
    else:
	return ("ok", "Details Available")
