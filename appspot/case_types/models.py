from django.utils.translation import ugettext_lazy as _
from django.db import models
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

class Case_type(models.Model):
	id = models.AutoField(primary_key=True)
	case_type = models.CharField(verbose_name=_('Case status'), max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='case_types')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('case_type')
		verbose_name_plural = _('case_types')