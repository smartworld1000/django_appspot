from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person
from appspot.companies.models import Company
from localflavor.us.models import USZipCodeField
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
ADDRESS_TYPE = (
	('HOME', _('Home')),
	('WORK', _('Work')),
	('OTHER', _('Other')),
)

class Address(models.Model):
	id = models.AutoField(primary_key=True) 
	person = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='addresses')
	company = models.ForeignKey(Company, blank=False, null=False, verbose_name=_('Company'), related_name='addresses')
	address_type = models.CharField(verbose_name=_('Address type'), max_length=100, choices=ADDRESS_TYPE)
	location_address = USZipCodeField(max_length=9, help_text=_(''), blank=False, null=False)
	address_label = models.CharField(verbose_name=_('Address label'), max_length=100, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(help_text=_(''))

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='addresses')['detail'], args=(self.id,))
	class Meta:
		verbose_name = _('address')
		verbose_name_plural = _('addresses')