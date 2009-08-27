from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.CharField(max_length=30)

    def __unicode__(self):
	return u"%s, %s" % (self.name, self.country)

class Category(models.Model):
    pass

class Products(models.Model):
    pass

class Price(models.Model):
    pass
