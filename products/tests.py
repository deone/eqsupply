import unittest
from products.models import *

class ProductsTestCase(unittest.TestCase):
    def setUp(self):
	self.division = Division.objects.create(name="Washing Machines", description="Machines used to wash")
	self.category = Category.objects.create(name="American Specs", description="Made in USA", division=self.division)
	self.product = Product.objects.create(name="Car Wash Simulator", description="", code="555", small_image="site_media/products/tool1.jpg", large_image="site_media/products/tool1.jpg", category=self.category, product_page="http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm")
	self.accessory = Accessory.objects.create(product=self.product, name="PC Interface Cable", description="PC Connection Wire", part_number="T2000567", image="", accessory_page="", cost="152.55")
	self.product_variation = ProductVariation.objects.create(product=self.product, part_number="S499989", description="Car Wash Simulator", cost="122.34")

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
	self.assertEquals(self.product.small_image, "site_media/products/tool1.jpg")
	self.assertEquals(self.product.large_image, "site_media/products/tool1.jpg")
	self.assertEquals(self.product.category, self.category)
	self.assertEquals(self.product.product_page, "http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm")

    def test_accessory(self):
	self.assertEquals(self.accessory.product, self.product)
	self.assertEquals(self.accessory.name, "PC Interface Cable")
	self.assertEquals(self.accessory.description, "PC Connection Wire")
	self.assertEquals(self.accessory.part_number, "T2000567")
	self.assertEquals(self.accessory.image, "")
	self.assertEquals(self.accessory.accessory_page, "")
	self.assertEquals(self.accessory.cost, "152.55")

    def test_product_variation(self):
	self.assertEquals(self.product_variation.product, self.product)
	self.assertEquals(self.product_variation.part_number, "S499989")
	self.assertEquals(self.product_variation.description, "Car Wash Simulator")
	self.assertEquals(self.product_variation.cost, "122.34")

    def tearDown(self):
	self.division.delete()
	self.category.delete()
	self.product.delete()
	self.accessory.delete()
	self.product_variation.delete()
