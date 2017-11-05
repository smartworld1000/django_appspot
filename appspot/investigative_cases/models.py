from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person

# Create your models here.
class Investigative_case(models.Model):
	id = models.AutoField(primary_key=True)
	case_number = models.CharField(verbose_name=_('Case number'), max_length=100, blank=False, null=False)
	claim_number = models.CharField(verbose_name=_('Claim number'), max_length=100, blank=False, null=False)
	injury_date = models.DateField(help_text=_(''))
	injury = models.CharField(verbose_name=_('Injury'), max_length=100, blank=False, null=False)
	file_received_date = models.DateField(help_text=_(''))
	case_type = models.CharField(verbose_name=_('Case type'), max_length=100, blank=False, null=False)
	client = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='cases_client')
	primary_subject = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='cases_primary_subject')
	case_status = models.CharField(verbose_name=_('Case status'), max_length=100, blank=False, null=False)
	case_description = models.TextField(verbose_name=_('Case description'), max_length=500, blank=False, null=False)
	case_dollar_budget = models.CharField(verbose_name=_('Case dollar budget'), max_length=100, blank=False, null=False)
	case_time_budget = models.CharField(verbose_name=_('Case time budget'), max_length=100, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(auto_now_add=True, help_text=_(''))
	primary_investigator = models.IntegerField(verbose_name=_('Primary investigator'), unique=False, blank=False, null=False)
	is_active = models.BooleanField(help_text=_(''))

	class Meta:
		verbose_name = _('investigative_case')
		verbose_name_plural = _('investigative_cases')