from django.utils.translation import ugettext_lazy as _
from django.db import models
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Case_video(models.Model):
	id = models.AutoField(primary_key=True)
	media_id = models.IntegerField(verbose_name=_('Media ID'), unique=False, blank=False, null=False)
	update_id = models.IntegerField(verbose_name=_('Update ID'), unique=False, blank=False, null=False)
	url = models.CharField(verbose_name=_('Url'), max_length=100, blank=False, null=False)
	file_name = models.CharField(verbose_name=_('File name'), max_length=100, blank=False, null=False)
	media_pin = models.IntegerField(verbose_name=_('Media pin'), unique=False, blank=False, null=False)

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='case_videos')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('case_video')
		verbose_name_plural = _('case_videos')