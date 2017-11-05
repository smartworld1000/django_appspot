from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person
from localflavor.us.models import PhoneNumberField

# Create your models here.
PHONE_TYPE = (
	('HOME', _('Home')),
	('WORK', _('Work')),
	('FAX', _('Fax')),
	('MOBILE', _('Mobile')),
	('OTHER', _('Other')),
)

class Phone_number(models.Model):
	id = models.AutoField(primary_key=True) 
	person = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='phone_numbers')
	phone_type = models.CharField(verbose_name=_('Phone type'), max_length=100, choices=PHONE_TYPE)
	number = PhoneNumberField(max_length=100, blank=False, help_text=_(''))
	phone_label = models.CharField(verbose_name=_('Phone label'), max_length=100, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(help_text=_(''))

	class Meta:
		verbose_name = _('phone_number')
		verbose_name_plural = _('phone_numbers')