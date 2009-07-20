from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings

from account.forms import SignupForm, LoginForm

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
	subject = "Registration: AERIX EQUIPMENT SUPPLY"
	message = "This is your activation link:\n\n%s" % activation_link
	sender = "no-reply@aerixnigeria.com"

	send_mail(subject, message, sender, email_list, fail_silently=False)

def create_activation_link(reg_id):
	url = settings.BASE_URL + "account/activate/?reg_id=%s" % reg_id
	return url

def activate(request):
	reg_id = request.GET['reg_id']
	print reg_id

	return render_to_response("account/activate.html", {
	}, context_instance=RequestContext(request))
