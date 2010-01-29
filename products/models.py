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
    code = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="/tmp")
    category = models.ForeignKey(Category)

    def __unicode__(self):
	return u"%s" % self.name
