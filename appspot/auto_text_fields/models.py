from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.auto_texts.models import Auto_text
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Auto_text_field(models.Model):
	id = models.AutoField(primary_key=True)
	parent_auto_text_field = models.ForeignKey(Auto_text, blank=False, null=False, verbose_name=_('Auto_text'), related_name='fields')
	field_name = models.CharField(verbose_name=_('Text'), max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.label
		
	def get_absolute_url(self):
		return reverse(get_url_names(prefix='auto_text_fields')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('auto_text_field')
		verbose_name_plural = _('auto_text_fields')