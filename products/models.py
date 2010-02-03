from django.db import models
from django.utils.translation import ugettext_lazy as _

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

class Accessories(CommonInfo):
    product = models.ForeignKey(Product)
    code = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="site_media/products/accessories")
    product_page = models.CharField(max_length=255)

    def __unicode__(self):
	return u"%s" % self.name
