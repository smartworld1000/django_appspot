from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.invoices.models import Invoice
from appspot.expense_types.models import Expense_type

# Create your models here.
class Invoice_items(models.Model):
	id = models.AutoField(primary_key=True)
	invoice =  models.ForeignKey(Invoice, blank=False, null=False, verbose_name=_('Invoice'), related_name='invoice_items')
	service_date = models.DateField(help_text=_(''), blank=False, null=False)
	service_end_date = models.DateField(auto_now_add=True, help_text=_(''), blank=False, null=False)
	item = models.ForeignKey(Expense_type, blank=False, null=False, verbose_name=_('Expense type'), related_name='line_items')
	quantity = models.FloatField(verbose_name=_('Quantity'), unique=False, blank=False, null=False)
	line_description = models.CharField(verbose_name=_('Line description'), max_length=100, blank=False, null=False)
	rate = models.FloatField(verbose_name=_('Rate'), unique=False, blank=False, null=False)
	amount = models.FloatField(verbose_name=_('Amount'), unique=False, blank=False, null=False)
	item_number = models.IntegerField(verbose_name=_('Item number'), unique=False, blank=False, null=False)

	class Meta:
		verbose_name = _('invoice_item')
		verbose_name_plural = _('invoice_items')