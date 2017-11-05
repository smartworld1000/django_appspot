from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.invoices.models import Invoice

# Create your models here.
class Payment(models.Model):
	id = models.AutoField(primary_key=True)
	invoice = models.ForeignKey(Invoice, blank=False, null=False, verbose_name=_('Invoice'), related_name='payments')
	payment_date = models.DateField(help_text=_(''), blank=False, null=False)
	method = models.CharField(verbose_name=_('Method'), max_length=100, blank=False, null=False)
	reference = models.CharField(verbose_name=_('Reference'), max_length=100, blank=False, null=False)
	amount = models.FloatField(verbose_name=_('Amount'), unique=False, blank=False, null=False)

	class Meta:
		verbose_name = _('payment')
		verbose_name_plural = _('payments')