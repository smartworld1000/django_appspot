from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person
from localflavor.us.models import USZipCodeField

# Create your models here.
class Vehicle(models.Model):
	id = models.AutoField(primary_key=True)
	person = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='vehicles')
	year = models.CharField(verbose_name=_('Vehicle'), max_length=100, blank=False, null=False)
	make = models.CharField(verbose_name=_('Make'), max_length=100, blank=False, null=False)
	model = models.CharField(verbose_name=_('Model'), max_length=100, blank=False, null=False)
	color = models.CharField(verbose_name=_('Color'), max_length=100, blank=False, null=False)
	vin = models.CharField(verbose_name=_('Vin'), max_length=100, blank=False, null=False)
	plate = models.CharField(verbose_name=_('Plate'), max_length=100, blank=False, null=False)
	plate_expiration = models.DateField(help_text=_(''))
	primary_owner = models.CharField(verbose_name=_('Primary owner'), max_length=100, blank=False, null=False)
	secondary_owner = models.CharField(verbose_name=_('Secondary owner'), max_length=100, blank=False, null=False)
	registered_address = USZipCodeField(max_length=9, help_text=_(''), blank=False, null=False)
	description = models.CharField(verbose_name=_('Description'), max_length=100, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(help_text=_(''))

	class Meta:
		verbose_name = _('vehicle')
		verbose_name_plural = _('vehicles')