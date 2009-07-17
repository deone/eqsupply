from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

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
			email = form.save()
			send_mail("Registration", "This is your activation link", "no-reply@aerixnigeria.com", [email], fail_silently=False)
			# Redirect and inform user of sucess
	else:
		form = SignupForm()

	return render_to_response("account/signup.html", {
		"form": form,
	})
