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

	def save(self):
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		email = self.cleaned_data['email']
		phone = self.cleaned_data['phone']
		username = self.cleaned_data['username']
		password = self.cleaned_data['password1']
		company = self.cleaned_data['company']
		company_address = self.cleaned_data['company_address']

		new_user = User(first_name=first_name, last_name=last_name, email=email, phone=phone, username=username, \
							password=password, company=company, company_address=company_address)

		new_user.save()
		return email
