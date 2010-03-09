from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVariant

from eqsupply.helpers import format_date

class Quotation(models.Model):
    user = models.ForeignKey(User)
    time_created = models.DateTimeField()
    quotation_no = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.BooleanField(default=False)	# Remember to set this flag to True when the quote is sent to email

    def to_dict(self):
	return {
	    "id": int(self.id),
	    "user_id": int(self.user.id),
	    "time_created": str(self.time_created),
	    "quotation_no": self.quotation_no,
	    "line_items": self.lineitem_set.all(),
	    "cost": str(self.cost),
	    "status": self.status
	}

    def line_item_qty(self):
	return {
	    "date_created": format_date(str(self.time_created.date())),
	    "line_item_qty": self.lineitem_set.all().count()
	}

    def __unicode__(self):
	return u"%s, %s" % (self.quotation_no, self.cost)

class LineItem(models.Model):
    quotation = models.ForeignKey(Quotation)
    product = models.ForeignKey(ProductVariant)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):
	return u"%s, %s, %s" % (self.product.part_number, self.quantity, self.cost)

class Cost(models.Model):
    """Includes, courier charges, custom charges (int'l & local) and insurance costs (if any)
       Updated, based on a defined algorithm, at the same time with QuoteItem."""
    pass
