from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

class Account(models.Model):
    user = models.ForeignKey(User, unique=True, verbose_name=_("user"))
    reg_id = models.CharField(_("reg_id"), max_length=50)

    def __unicode__(self):
	return self.user.username
