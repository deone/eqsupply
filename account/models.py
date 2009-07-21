from django.db import models

import datetime

class User(models.Model):
	"""
	# Create users
	>>> deone = User.objects.create(first_name="Dayo", last_name="Osikoya", email="alwaysdeone@gmail.com", phone="08029299274", username="deone", password="deone", company="Aerix", company_address="9, Olosa Street", reg_id="deonedune369")
	>>> assert deone.first_name == "Dayo"
	>>> assert deone.last_name == "Osikoya"
	>>> assert deone.company_address == "9, Olosa Street"
	>>> assert deone.reg_id == "deonedune369"
	"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	username = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=128)
	company = models.CharField(max_length=100)
	company_address = models.CharField(max_length=255)
	date_joined = models.DateTimeField(default=datetime.datetime.now)
	last_login = models.DateTimeField(default= datetime.datetime.now)
	reg_id = models.CharField(max_length=255)

	def __unicode__(self):
		return self.username
