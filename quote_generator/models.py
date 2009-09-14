from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=30)

    def __unicode__(self):
	return u"%s" % (self.name)

    class Meta:
	verbose_name_plural = "manufacturers"

class CommonInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_description = models.TextField()

    class Meta:
	abstract=True

class Category(CommonInfo):
    pass

    def __unicode__(self):
	return u"%s" % self.name

    class Meta:
	verbose_name_plural = "categories"

class Product(CommonInfo):
    code = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer)
    categories = models.ManyToManyField(Category)
    product_page = models.CharField(max_length=30)
    specs_page = models.CharField(max_length=30)

    def __unicode__(self):
	return u"%s %s" % (self.code, self.name)

    class Meta:
	verbose_name_plural = "products"

class Quote(models.Model):
    # Add status flag to know whether the quote has been completed and sent or not
    # If it has been completed, it would not be displayed on the home page,
    # Else, it would be displayed so that the user can add more items to it.
    user = models.ForeignKey(User)
    description = models.TextField()
    quote_cost = models.IntegerField()

    def __unicode__(self):
	return u"%s, %s" % (self.description, self.quote_cost)
    

class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    quote_item_cost = models.IntegerField()

    def __unicode__(self):
	return u"%s, %s" % (self.product, self.quantity)
