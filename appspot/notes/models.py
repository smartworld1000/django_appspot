from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.notes_headers.models import Notes_header

# Create your models here.
class Note(models.Model):
	id = models.AutoField(primary_key=True)
	notes = models.ForeignKey(Notes_header, blank=False, null=False, verbose_name=_('Notes header'), related_name='notes')
	note_time = models.DateTimeField(help_text=_(''), blank=False, null=False)
	note_text = models.CharField(verbose_name=_('Note text'), max_length=100, blank=False, null=False)
	time_sort_field = models.CharField(verbose_name=_('Time sort field'), max_length=100, blank=False, null=False)
	military = models.IntegerField(verbose_name=_('Military'), unique=False, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(help_text=_(''), blank=False, null=False)

	class Meta:
		verbose_name = _('note')
		verbose_name_plural = _('notes')