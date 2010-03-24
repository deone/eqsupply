import unittest
import datetime

from django.contrib.auth.models import User

from products.models import *
from quote.models import *

class EqsupplyTestCase(unittest.TestCase):
    def setUp(self):
	# Account objects, we need to test the account model.
	self.user = User.objects.create_user(username="deone", email="alwaysdeone@yahoo.com", password="deone")	
	
	# Products, we need to test product images properly.
	self.division = Division.objects.create(name="Washing Machines", description="Machines used to wash")
	self.category = Category.objects.create(name="American Specs", description="Made in USA", division=self.division)
	self.product = Product.objects.create(name="Car Wash Simulator", description="", code="555", small_image="site_media/products/tool1.jpg", large_image="site_media/products/tool1.jpg", category=self.category, product_page="http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm")
	self.accessory = Accessory.objects.create(product=self.product, name="PC Interface Cable", description="PC Connection Wire", part_number="T2000567", image="", accessory_page="", cost="152.55")
	self.product_variant = ProductVariant.objects.create(product=self.product, part_number="S499989", description="Car Wash Simulator", cost="122.34")

	# Quote
	self.quantity = 20
	self.quotation = Quotation.objects.create(user=self.user, time_created=datetime.datetime.now(), quotation_no="AGS 03-01-01", cost="120.00", status=False)
	self.line_item = LineItem.objects.create(quotation=self.quotation, product=self.product_variant, quantity=self.quantity, cost_per_unit=self.product_variant.cost, cost=str(float(self.product_variant.cost) * self.quantity))

    def tearDown(self):
	self.user.delete()

	self.division.delete()
	self.category.delete()
	self.product.delete()
	self.accessory.delete()
	self.product_variant.delete()

	self.quotation.delete()
	self.line_item.delete()
