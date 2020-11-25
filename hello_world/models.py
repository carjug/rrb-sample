from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=120)
    address_unit = models.CharField(max_length=10)
    address_city = models.CharField(max_length=30)
    address_state = models.CharField(max_length=2, choices=state choices list somewhere)
    address_zip_code = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=11)
    # social_security = unknown how to store this yet


class Application(models.Model):
    class ApplicationType(models.TextChoices):
        SICKNESS = 'SI', _('Sickness')
        UNKNOWN = 'UN', _('Unknown')

    person = models.ForeignKey(
        Person,
        models.SET_NULL,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    type = models.CharField(
        max_length=20,
        choices=ApplicationType.choices
    )



