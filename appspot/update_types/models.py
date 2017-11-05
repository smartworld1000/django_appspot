from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Update_type(models.Model):
	id = models.AutoField(primary_key=True)
	update_type = models.CharField(verbose_name=_('Update type'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('update_type')
		verbose_name_plural = _('update_types')	