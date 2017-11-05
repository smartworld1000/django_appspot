from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.expense_types.models import Expense_type
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Contractor_rate(models.Model):
	id = models.AutoField(primary_key=True)
	expense_type = models.ForeignKey(Expense_type, blank=False, null=False, verbose_name=_('Expense_type'), related_name='contractor_rates')
	investigator_id = models.IntegerField(verbose_name=_('Investigator ID'), unique=False, blank=False, null=False)
	rate = models.FloatField(verbose_name=_('Rate'), unique=False, blank=False, null=False)

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='contractor_rates')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('contractor_rate')
		verbose_name_plural = _('contractor_rates')