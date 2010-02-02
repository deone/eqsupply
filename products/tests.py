import unittest
from products.models import *

class ProductsTestCase(unittest.TestCase):
    def setUp(self):
	self.division = Division.objects.create(name="Washing Machines", description="Machines used to wash")
	self.category = Category.objects.create(name="American Specs", description="Made in USA", division=self.division)
	self.product = Product.objects.create(name="Car Wash Simulator", description="", code="555", image="site_media/products/tool1.jpg", category=self.category)

    def test_division(self):
	self.assertEquals(self.division.name, "Washing Machines")
	self.assertEquals(self.division.description, "Machines used to wash")

    def test_category(self):
	self.assertEquals(self.category.name, "American Specs")
	self.assertEquals(self.category.description, "Made in USA")
	self.assertEquals(self.category.division, self.division)

    def test_product(self):
	self.assertEquals(self.product.name, "Car Wash Simulator")
	self.assertEquals(self.product.description, "")
	self.assertEquals(self.product.code, "555")
	self.assertEquals(self.product.image, "site_media/products/tool1.jpg")
	self.assertEquals(self.product.category, self.category)

    def tearDown(self):
	self.division.delete()
	self.category.delete()
	self.product.delete()
