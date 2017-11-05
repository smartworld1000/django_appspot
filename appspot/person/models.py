from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.companies.models import Company
from localflavor.us.models import USSocialSecurityNumberField

# Create your models here.
GENDER = (
	('male', _('Male')),
	('female', _('Female')),
)

PERSON_TYPE = (
	('CLIENT', _('Client')),
	('SUBJECT', _('Subject')),
	('ASSOCIATE', _('Associate')),
	('RELATIVE', _('Relative')),
	('OTHER', _('Other')),
)

class Person(models.Model):
	id = models.AutoField(primary_key=True)
	prefix = models.CharField(verbose_name=_('Prefix'), max_length=100, blank=False, null=False)
	first_name = models.CharField(verbose_name=_('First name'), max_length=100, blank=False, null=False)
	last_name = models.CharField(verbose_name=_('Last name'), max_length=100, blank=False, null=False)
	middle_name = models.CharField(verbose_name=_('Middle name'), max_length=100, blank=False, null=False)
	suffix = models.CharField(verbose_name=_('Suffix'), max_length=100, blank=False, null=False)
	social_security_number = USSocialSecurityNumberField(help_text=_(''))
	date_of_birth = models.DateField(help_text=_(''))
	gender = models.CharField(verbose_name=_('Gender'), max_length=100, choices=GENDER)
	race = models.CharField(verbose_name=_('Race'), max_length=100, blank=False, null=False)
	height = models.FloatField(help_text=_(''))
	weight = models.FloatField(help_text=_(''))
	hair = models.CharField(verbose_name=_('Hair'), max_length=100, blank=False, null=False)
	build = models.CharField(verbose_name=_('Build'), max_length=100, blank=False, null=False)
	eyes = models.CharField(verbose_name=_('Eyes'), max_length=100, blank=False, null=False)
	glasses = models.CharField(verbose_name=_('Glasses'), max_length=100, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(auto_now_add=True, help_text=_(''))
	person_type = models.CharField(verbose_name=_('Person type'), max_length=100, choices=PERSON_TYPE)
	company = models.ForeignKey(Company, blank=False, null=False, verbose_name=_('Company'), related_name='company_contacts')
	investigative_case = models.CharField(verbose_name=_('Investigative case'), max_length=100, blank=False, null=False)
	is_active = models.BooleanField(help_text=_(''))
	relationship = models.CharField(verbose_name=_('Relationship'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('person')
		verbose_name_plural = _('person')