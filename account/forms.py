from django import forms

from account.models import User

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
	company_address = forms.CharField(label="Company Address", widget=forms.TextInput())
