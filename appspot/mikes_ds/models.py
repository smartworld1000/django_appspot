from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Mike_ds(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(verbose_name=_('First name'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('mike_ds')
		verbose_name_plural = _('mike_ds')