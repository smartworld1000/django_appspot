from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person
from appspot.investigative_cases.models import Investigative_case

# Create your models here.
class Invoice(models.Model):
	id = models.AutoField(primary_key=True)
	invoce_date = models.DateField(help_text=_(''), blank=False, null=False)
	terms = models.CharField(verbose_name=_('Terms'), max_length=100, blank=False, null=False)
	term_days = models.IntegerField(verbose_name=_('Term days'), unique=False, blank=False, null=False)
	due = models.CharField(verbose_name=_('Due'), max_length=100, blank=False, null=False)
	invoice_number = models.IntegerField(verbose_name=_('Invoice number'), unique=False, blank=False, null=False)
	customer = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='invoices')
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative case'), related_name='invoices')
	total = models.FloatField(verbose_name=_('Total'), unique=False, blank=False, null=False)

	class Meta:
		verbose_name = _('invoice')
		verbose_name_plural = _('invoices')