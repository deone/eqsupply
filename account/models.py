from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

class Account(models.Model):
    user = models.ForeignKey(User, unique=True, verbose_name=_("user"))
    reg_id = models.CharField(_("reg_id"), max_length=50)
    phone = models.CharField(max_length=15, unique=True, null=True)
    company = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    company_street_address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __unicode__(self):
	return self.user.username
