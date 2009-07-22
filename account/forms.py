from django import forms

from account.models import UserAccount

import hashlib
import datetime
import string
import random

class LoginForm(forms.Form):
	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput())
	password = forms.CharField(label="Password", widget= forms.PasswordInput(render_value=False))


class SignupForm(forms.Form):
	first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput())
	last_name = forms.CharField(label="Last Name", max_length=30, widget=forms.TextInput())
	email = forms.EmailField(label="Email", widget=forms.TextInput())
	phone = forms.CharField(label="Phone Number", max_length=15, widget=forms.TextInput())
	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput())
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput(render_value=False))
	company = forms.CharField(label="Company", widget=forms.TextInput())
	position = forms.CharField(label="Position", widget=forms.TextInput())
	company_street_address = forms.CharField(label="Company Street Address", widget=forms.TextInput())
	city = forms.CharField(label="City", widget=forms.TextInput())
	country = forms.CharField(label="Country", widget=forms.TextInput())

	def save(self):
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		email = self.cleaned_data['email']
		phone = self.cleaned_data['phone']
		username = self.cleaned_data['username']
		enc_type = "sha1"
		salt = "".join(random.sample(string.letters+string.digits, 5))
		password = enc_type + "$" + salt + "$" + hashlib.sha1(salt + self.cleaned_data['password1']).hexdigest()
		company = self.cleaned_data['company']
		position = self.cleaned_data['position']
		company_street_address = self.cleaned_data['company_street_address']
		city = self.cleaned_data['city']
		country = self.cleaned_data['country']
		reg_id = hashlib.sha1(email + ":" + password + ":"  + str(datetime.datetime.now())).hexdigest()
		is_active = 0

		new_user = UserAccount.objects.create(first_name=first_name, \
						last_name=last_name, email=email, phone=phone, \
						username=username, password=password, \
						company=company, position=position,\
						company_street_address=company_street_address, \
						city=city, country=country, reg_id=reg_id, \
						is_active=is_active)

		return email, reg_id
