from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings

from account.forms import SignupForm, LoginForm

import datetime
import md5

def login(request):

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect()
	else:
		form = LoginForm()

	return render_to_response("account/login.html", {
		"form": form,
	})

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			email, password = form.save()
			email_user(email, password)
			request.flash['feedback'] = "Registration successful. An activation email has been sent to %s." % email
			return HttpResponseRedirect(reverse("acct_signup"))
	else:
		form = SignupForm()

	return render_to_response("account/signup.html", {
		"form": form,
	}, context_instance=RequestContext(request))

def email_user(email, password):
	activation_link = create_activation_link(email, password)
	email_list = []
	email_list.append(email)
	subject = "Registration: AERIX EQUIPMENT SUPPLY"
	message = "This is your activation link:\n\n%s" % activation_link
	sender = "no-reply@aerixnigeria.com"

	send_mail(subject, message, sender, email_list, fail_silently=False)

def create_activation_link(email, password):
	hashed = md5.new()
	hashed.update(email + ":" + password + ":" + str(datetime.datetime.now()))
	reg_id = hashed.hexdigest()
	url = settings.BASE_URL + "account/activate?regid=%s" % reg_id
	return url

def activate(request):
	pass
