from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from account.forms import SignupForm, LoginForm

def login(request):

	if request.method == "POST":
		form = form_class(request.POST)
		if form.is_valid():
			return HttpResponseRedirect()
	else:
		form = LoginForm()

	return render_to_response("account/login.html", {
		"form": form,
	})

def signup(request):

	if request.method == "POST":
		form = form_class(request.POST)
		if form.is_valid():
			return HttpResponseRedirect()
	else:
		form = SignupForm()

	return render_to_response("account/signup.html", {
		"form": form,
	})
