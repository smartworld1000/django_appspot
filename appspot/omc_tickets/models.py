from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Omc_ticket(models.Model):
	id = models.AutoField(primary_key=True)
	ticket_number = models.IntegerField(verbose_name=_('Ticket number'), unique=False, blank=False, null=False)
	status = models.CharField(verbose_name=_('Status'), max_length=100, blank=False, null=False)
	date_opened = models.DateTimeField(help_text=_(''), blank=False, null=False)
	label = models.CharField(verbose_name=_('Label'), max_length=100, blank=False, null=False)
	description = models.TextField(verbose_name=_('Description'), max_length=500, blank=False, null=False)
	resolution = models.TextField(verbose_name=_('Resolution'), max_length=500, blank=False, null=False)
	date_closed = models.DateTimeField(auto_now_add=True, help_text=_(''), blank=False, null=False)

	class Meta:
		verbose_name = _('omc_ticket')
		verbose_name_plural = _('omc_tickets')