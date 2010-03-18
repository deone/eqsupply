from django.db import IntegrityError

from eqsupply.products.models import *
from eqsupply.test_helpers import EqsupplyTestCase 

class ProductsTests(EqsupplyTestCase):
    def test_division(self):
	# content
	self.failUnless(self.division.name == "Washing Machines")
	self.failUnless(self.division.description != "Machines")

	# type
	self.failIf(isinstance(self.division.name, int))
	self.failUnless(isinstance(self.division.description, str))

	# constraints
	self.failUnlessRaises(IntegrityError, Division.objects.create, name="Washing Machines", description="")	# unique

    # Start here
    def test_category(self):
	self.assert_(self.category.name == "American Specs")
	self.assert_(self.category.description == "Made in USA")
	self.failUnless(self.category.division == self.division)

    def test_product(self):
	# content
	self.assert_(self.product.name == "Car Wash Simulator")
	self.assert_(self.product.description == "")
	self.assert_(self.product.code == "555")
	self.assert_(self.product.small_image == "site_media/products/tool1.jpg")
	self.assert_(self.product.large_image == "site_media/products/tool1.jpg")
	self.assert_(self.product.category == self.category)
	self.assert_(self.product.product_page == "http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm")

	# types
	# constraints: unique code, 
	# images

    def test_accessory(self):
	# content
	self.assert_(self.accessory.product == self.product)
	self.assert_(self.accessory.name == "PC Interface Cable")
	self.assert_(self.accessory.description == "PC Connection Wire")
	self.assert_(self.accessory.part_number == "T2000567")
	self.assert_(self.accessory.image == "")
	self.assert_(self.accessory.accessory_page == "")
	self.assert_(self.accessory.cost == "152.55")

	# type
	# ...

    def test_product_variant(self):
	self.assert_(self.product_variant.product == self.product)
	self.assert_(self.product_variant.part_number == "S499989")
	self.assert_(self.product_variant.description == "Car Wash Simulator")
	self.assert_(self.product_variant.cost == "122.34")
