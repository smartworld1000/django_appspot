from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Expense_type(models.Model):
	id = models.AutoField(primary_key=True)
	expense_type = models.CharField(verbose_name=_('Expense type'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('expense_type')
		verbose_name_plural = _('expense_types')