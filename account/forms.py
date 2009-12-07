from django import forms
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.auth.models import User

import hashlib
import datetime
import string
import random

import re

alnum_re = re.compile(r'^\w+$')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", max_length=30, widget=forms.TextInput())
    password = forms.CharField(label="Password:", widget= forms.PasswordInput(render_value=False))

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
        login(request, self.user)
        return True

class SignupForm(forms.Form):
    first_name = forms.CharField(label=_("First Name:"), max_length=30, widget=forms.TextInput())
    last_name = forms.CharField(label=_("Last Name:"), max_length=30, widget=forms.TextInput())
    username = forms.CharField(label=_("Username:"), max_length=30, widget=forms.TextInput())
    password1 = forms.CharField(label=_("Password:"), widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label=_("Password (again):"), widget=forms.PasswordInput(render_value=False))
    email = forms.EmailField(label=_("Email:"), widget=forms.TextInput())

    def clean_username(self):
	if not alnum_re.search(self.cleaned_data["username"]):
	    raise forms.ValidationError(_("Usernames can only contain letters, numbers and underscores."))
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
	hash = hashlib.md5(new_user.email + ":" + password + str(datetime.datetime.now()))
	new_user.account_set.create(reg_id=hash)
	new_user.first_name = firstname
	new_user.last_name = lastname
	new_user.is_active = False
	new_user.save()

	return new_user
