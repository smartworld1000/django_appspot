from django.utils.translation import ugettext_lazy as _
from django.db import models
from localflavor.us.models import USZipCodeField
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Company(models.Model):
	id = models.AutoField(primary_key=True)
	company_name = models.CharField(verbose_name=_('Prefix'), max_length=100, blank=False)
	company_address = USZipCodeField(max_length=9, help_text=_(''), blank=False, null=False)
	
	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='companies')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('company')
		verbose_name_plural = _('companies')