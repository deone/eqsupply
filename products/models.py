from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
	abstract = True

class Category(CommonInfo):
    def __unicode__(self):
	return u"%s" % self.name

    class Meta:
	verbose_name_plural = "categories"

class Subcategory(CommonInfo):
    category = models.ForeignKey(Category)

    def __unicode__(self):
	return u"%s" % self.name

    class Meta:
	verbose_name_plural = "subcategories"
