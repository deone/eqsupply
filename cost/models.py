from django.db import models

class Weight(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=1)

    def __unicode__(self):
	return self.weight

class Zone(models.Model):
    zone = models.IntegerField()
    weights = models.ManyToManyField(Weight, through="Cost")

    def __unicode__(self):
	return self.zone

class Location(models.Model):
    zone = models.ForeignKey(Zone)
    name = models.CharField(max_length=20)

    def __unicode__(self):
	return self.name

class Cost(models.Model):
    weight = models.ForeignKey(Weight)
    zone = models.ForeignKey(Zone)
    cost = models.IntegerField()
