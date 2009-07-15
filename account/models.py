from django.db import models

import datetime

class User(models.Model):
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

	def __unicode__(self):
		return self.username

	def is_authenticated(self):
		return True

	def get_full_name(self):
		full_name = u'%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def set_password(self, raw_password):
		import random
		algo = 'sha1'
		salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
		hsh = get_hexdigest(algo, salt, raw_password)
		self.password = '%s$%s$%s' % (algo, salt, hsh)
