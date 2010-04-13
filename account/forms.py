from django import forms
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from eqsupply.cost.models import Location

import hashlib
import datetime
import string
import random

import re

alnum_re = re.compile(r'^\w+$')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput())
    password = forms.CharField(max_length=30, widget= forms.PasswordInput(render_value=False))

    user = None

    def clean(self):
        if self._errors:
            return
        username = self.cleaned_data["username"] 
        password = self.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_active:
                raise forms.ValidationError("You have not activated your account")
            else:
                self.user = user
        else:
            raise forms.ValidationError("Wrong Username and Password Combination")
        return self.cleaned_data

    def login(self, request):
	if self.is_valid():
	    login(request, self.user)
	    return True
	return False

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput())
    last_name = forms.CharField(max_length=30, widget=forms.TextInput())
    username = forms.CharField(max_length=30, widget=forms.TextInput())
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label=_("Password (again)"), widget=forms.PasswordInput(render_value=False))
    email = forms.EmailField(widget=forms.TextInput())

    def clean_username(self):
	if not alnum_re.search(self.cleaned_data["username"]):
	    raise forms.ValidationError(_("Usernames can only contain letters, numbers and underscores."))
	if len(self.cleaned_data["username"]) < 6:
	    raise forms.ValidationError(_("Username must be at least 6 characters long."))
	try:
	    user = User.objects.get(username__iexact=self.cleaned_data["username"])
	except User.DoesNotExist:
	    return self.cleaned_data["username"]
	raise forms.ValidationError(_("This username is already taken. Please choose another."))

    def clean(self):
	if "password1" in self.cleaned_data and "password2" in self.cleaned_data:
	    if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
		raise forms.ValidationError(_("Your password entries must be the same."))
	return self.cleaned_data

    def save(self):
	firstname = self.cleaned_data['first_name']
	lastname = self.cleaned_data['last_name']
	username = self.cleaned_data['username']
	email = self.cleaned_data['email']
	password = self.cleaned_data["password1"]

	new_user = User.objects.create_user(username, email, password)
	hash = hashlib.md5(email + ":" + password + str(datetime.datetime.now())).hexdigest()
	new_user.account_set.create(reg_id=hash)
	new_user.first_name = firstname
	new_user.last_name = lastname
	new_user.is_active = False
	new_user.save()

	return new_user

def fetch_locations():
    return [(location.id, location.name) for location in Location.objects.all()]

class UserDetailForm(forms.Form):
    phone = forms.CharField(max_length=11, widget=forms.TextInput())
    company = forms.CharField()
    position = forms.CharField()
    company_street_address = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    location = forms.ChoiceField(choices=fetch_locations())
