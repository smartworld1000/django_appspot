from django.utils.translation import ugettext_lazy as _
from django.db import models
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Case_sequence(models.Model):
	id = models.AutoField(primary_key=True)
	case_year = models.IntegerField(verbose_name=_('Case year'), unique=False, blank=False, null=False)
	case_sequence_number = models.IntegerField(verbose_name=_('Sequence number'), unique=False, blank=False, null=False)
	case_number = models.CharField(verbose_name=_('Number'), max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='case_sequnces')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('case_sequence')
		verbose_name_plural = _('case_sequences')