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
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200, blank=True, null=True)
    quote_cost = models.IntegerField(default=0)	# Update this when the user previews the quote, just before sending it to email
    time_created = models.DateTimeField()	# The time the blank quote was created
    status = models.BooleanField(default=False)	# Remember to set this flag to True when the quote is sent to email

    def __unicode__(self):
	return u"%s, %s" % (self.title, self.quote_cost)

    def todict(self):
	return {
	    "id": int(self.id),
	    "user_id": int(self.user.id),
	    "title": self.title,
	    "quote_cost": self.quote_cost,
	    "time_created": str(self.time_created),
	    "status": self.status
	}

class Price(models.Model):
    # Let's plug you in later
    product = models.ForeignKey(Product)
    product_cost = models.IntegerField()
    shipping_cost = models.IntegerField()

    def __unicode__(self):
	return u"%s" % self.product_cost

class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    quote_item_cost = models.IntegerField()
    #quote_item_cost = models.ForeignKey(Price)

    def __unicode__(self):
	return u"%s, %s" % (self.product, self.quantity)
