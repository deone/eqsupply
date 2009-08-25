from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings

from account.forms import SignupForm, LoginForm
from account.models import UserAccount

from eqsupply import helpers as h

@h.json_response
def login(request, **kwargs):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return ("ok", "Login Successful")

        return ("error", "Unable to Login")
    else:
        form = LoginForm()

        return render_to_response("account/login.html", {
            "form": form, 
        }, context_instance=RequestContext(request))

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			email, reg_id = form.save()
			email_user(email, reg_id)
			request.flash['feedback'] = "Registration successful. An activation email has been sent to %s." % email
			return HttpResponseRedirect(reverse("acct_signup"))
	else:
		form = SignupForm()

	return render_to_response("account/signup.html", {
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

	return render_to_response("account/activate.html", {
		"user": activated_user,
	}, context_instance=RequestContext(request))
