from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Relationship(models.Model):
	id = models.AutoField(primary_key=True)
	relationship = models.CharField(verbose_name=_('Relationship'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('relationship')
		verbose_name_plural = _('relationships')