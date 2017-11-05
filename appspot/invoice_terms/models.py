from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Invoice_term(models.Model):
	id = models.AutoField(primary_key=True)
	invoice_term = models.CharField(verbose_name=_('Invoice term'), max_length=100, blank=False, null=False)
	days = models.IntegerField(verbose_name=_('Days'), unique=False, blank=True, null=True)

	class Meta:
		verbose_name = _('invoice_term')
		verbose_name_plural = _('invoice_terms')