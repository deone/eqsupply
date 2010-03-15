from eqsupply.test_helpers import EqsupplyTestCase 

class ProductsTests(EqsupplyTestCase):
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

    def test_product_variant(self):
	self.assertEquals(self.product_variant.product, self.product)
	self.assertEquals(self.product_variant.part_number, "S499989")
	self.assertEquals(self.product_variant.description, "Car Wash Simulator")
	self.assertEquals(self.product_variant.cost, "122.34")
