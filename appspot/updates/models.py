from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case

# Create your models here.
class Update(models.Model):
	id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative case'), related_name='updates')
	activity_date = models.DateField(help_text=_(''), blank=False, null=False)
	activity_text = models.TextField(verbose_name=_('Activity text'), max_length=500, blank=False, null=False)
	last_sent = models.CharField(verbose_name=_('Last sent'), max_length=100, blank=False, null=False)
	vzaar_url = models.CharField(verbose_name=_('Vzzaar url'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('update')
		verbose_name_plural = _('updates')