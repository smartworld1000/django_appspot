from django.utils.translation import ugettext_lazy as _
from django.db import models
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Auto_text(models.Model):
	id = models.AutoField(primary_key=True)
	label = models.CharField(verbose_name=_('Label'), max_length=100, blank=False, null=False)
	atext = models.CharField(verbose_name=_('Text'), max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='auto_texts')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('auto_text')
		verbose_name_plural = _('auto_texts')