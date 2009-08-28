from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.CharField(max_length=30)

    def __unicode__(self):
	return u"%s, %s" % (self.name, self.country)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
	return u"%s" % self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
	return u"%s %s" % (self.code, self.name)
