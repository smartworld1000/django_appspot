from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case

# Create your models here.
class Notes_header(models.Model):
	id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative_case'), related_name='notes_headers')
	investigator_id = models.IntegerField(verbose_name=_('Investigator ID'), unique=False, blank=False, null=False)
	investigator_name = models.CharField(verbose_name=_('Investigator name'), max_length=100, blank=False, null=False)
	date_worked = models.DateField(help_text=_(''))
	weather = models.CharField(verbose_name=_('Weather'), max_length=100, blank=False, null=False)
	notes_summary = models.CharField(verbose_name=_('Notes summary'), max_length=100, blank=False, null=False)
	city = models.CharField(verbose_name=_('City'), max_length=100, blank=False, null=False)
	state = models.CharField(verbose_name=_('State'), max_length=100, blank=False, null=False)
	notes_complete = models.BooleanField(help_text=_(''))
	wunderground_temp = models.FloatField(help_text=_(''))

	class Meta:
		verbose_name = _('notes_header')
		verbose_name_plural = ('notes_headers')