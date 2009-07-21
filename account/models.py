from django.db import models

import datetime

class User(models.Model):
	"""
	# Create users
	>>> import md5
	>>> hashed = md5.new()
	>>> hashed.update("deone")
	>>> new_user = User(first_name="Dayo", last_name="Osikoya", email="alwaysdeone@gmail.com", phone="08029299274", username="deone", password=hashed.hexdigest(), company="Aerix", position="Procurement Officer", company_street_address="9, Olosa Street", city="Lagos", country="", reg_id="deonedune369")
	>>> assert new_user.first_name == "Dayo"
	>>> assert new_user.last_name == "Osikoya"
	>>> assert new_user.email == "alwaysdeone@gmail.com"
	>>> assert new_user.phone == "08029299274"
	>>> assert new_user.username == "deone"
	>>> assert new_user.password == hashed.hexdigest()
	>>> assert new_user.company == "Aerix"
	>>> assert new_user.position == "Procurement Officer"
	>>> assert new_user.company_street_address == "9, Olosa Street"
	>>> assert new_user.city == "Lagos"
	>>> assert new_user.country == ""
	>>> assert new_user.reg_id == "deonedune369"
	>>> assert new_user.is_activated == 0
	"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	username = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=128)
	company = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	company_street_address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100, null=True)
	reg_id = models.CharField(max_length=255)
	is_activated = models.BooleanField(default=0)
	date_joined = models.DateTimeField(default=datetime.datetime.now)
	last_login = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return self.username

	def activate(self):
		pass
