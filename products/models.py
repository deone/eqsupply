from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
	abstract = True

class Division(CommonInfo):
    def __unicode__(self):
	return u"%s" % self.name

class Category(CommonInfo):
    division = models.ForeignKey(Division)

    def __unicode__(self):
	return u"%s" % self.name

    class Meta:
	verbose_name_plural = "categories"

class Product(CommonInfo):
    category = models.ForeignKey(Category)
    code = models.CharField(max_length=50, unique=True)
    small_image = models.ImageField(upload_to="site_media/products/small")
    large_image = models.ImageField(upload_to="site_media/products/large")
    product_page = models.CharField(max_length=255)

    def __unicode__(self):
	return u"%s" % self.name

class Accessory(models.Model):
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    part_number = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="site_media/products/accessories", blank=True)
    accessory_page = models.CharField(max_length=255, blank=True)
    cost = models.CharField(max_length=10)

    def __unicode__(self):
	return u"%s - %s" % (self.description, self.product)

    class Meta:
	verbose_name_plural = "accessories"

class ProductVariant(models.Model):
    """Holds all part numbers and description of product variants. Many-to-one relationship with Product"""
    product = models.ForeignKey(Product)
    part_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):
	return u"%s - %s" % (self.product, self.part_number)
