from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVariant

class Quotation(models.Model):
    user = models.ForeignKey(User)
    time_created = models.DateTimeField()
    quotation_no = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.BooleanField(default=False)	# Remember to set this flag to True when the quote is sent to email

    def __unicode__(self):
	return "%s, %s" % (self.quotation_no, self.cost)

    def to_dict(self):
	"""We have to return dict values in unicode to make them JSON serializable"""
	return dict([(item[0], unicode(item[1])) for item in self.__dict__.iteritems()])

class LineItem(models.Model):
    quotation = models.ForeignKey(Quotation)
    product = models.ForeignKey(ProductVariant)
    quantity = models.IntegerField()
    cost_per_unit = models.DecimalField(max_digits=20, decimal_places=2)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    courier_charge_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    courier_charge = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __unicode__(self):
	return "%s, %s, %s" % (self.product.part_number, self.quantity, self.cost)
