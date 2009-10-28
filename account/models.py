from django.db import models
from django.contrib.auth.models import User, UserManager

class UserAccount(User):
    """
    >>> new_user = UserAccount.objects.create(username="deone", email="alwaysdeone@gmail.com", password="deone", phone="08029299274", company="Aerix", position="DBA", company_street_address = "9, Olosa Street", city="Lagos", state="Lagos", country="Nigeria", is_active=0)
    >>> assert new_user.username == "deone"
    >>> assert new_user.email == "alwaysdeone@gmail.com"
    >>> assert new_user.password == "deone"
    >>> assert new_user.phone == "08029299274"
    >>> assert new_user.company == "Aerix"
    >>> assert new_user.position == "DBA"
    >>> assert new_user.company_street_address == "9, Olosa Street"
    >>> assert new_user.city == "Lagos"
    >>> assert new_user.state == "Lagos"
    >>> assert new_user.country == "Nigeria"
    """
    phone = models.CharField(max_length=15, unique=True, null=True)
    company = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    company_street_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    reg_id = models.CharField(max_length=255)

    objects = UserManager()

    def __unicode__(self):
	return self.username

    class Meta:
	verbose_name_plural = "User Accounts"
