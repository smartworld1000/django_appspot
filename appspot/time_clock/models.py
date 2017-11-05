from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Time_clock(models.Model):
	id = models.AutoField(primary_key=True)
	payperiod = models.CharField(verbose_name=_('Pay period'), max_length=100, blank=False, null=False)
	workdate = models.DateField(help_text=_(''), blank=False, null=False)
	timein = models.DateTimeField(help_text=_(''), blank=False, null=False)
	timeout = models.DateTimeField(help_text=_(''), blank=False, null=False)
	original_timein = models.CharField(verbose_name=_('Original timein'), max_length=100, blank=False, null=False)
	original_timeout = models.CharField(verbose_name=_('Original timeout'), max_length=100, blank=False, null=False)
	hoursworked = models.FloatField(blank=False, null=False)

	class Meta:
		verbose_name = _('time_clock')
		verbose_name_plural = _('time_clock')