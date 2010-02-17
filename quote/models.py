from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVariation

class Quotation(models.Model):
    user = models.ForeignKey(User)
    time_created = models.DateTimeField()
    quotation_no = models.CharField(max_length=20)
    cost = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __unicode__(self):
	return u"%s, %s" % (self.quotation_no, self.cost)

class LineItem(models.Model):
    quotation = models.ForeignKey(Quotation)
    product = models.ForeignKey(ProductVariation)
    quantity = models.IntegerField()
    cost = models.IntegerField(default=0)

    def __unicode__(self):
	return u"%s, %s, %s" %s (self.product.part_number, self.quantity, self.cost)

class Cost(models.Model):
    """Includes, courier charges, custom charges (int'l & local) and insurance costs (if any)
       Updated, based on a defined algorithm, at the same time with QuoteItem."""
    pass
