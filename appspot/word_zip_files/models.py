from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Word_zip_file(models.Model):
	id = models.AutoField(primary_key=True)
	file_content = models.FileField(upload_to=None);
	file_name = models.CharField(verbose_name=_('File name'), max_length=100, blank=False, null=False)
	mime = models.CharField(verbose_name=_('Mime'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('word_zip_file')
		verbose_name_plural = _('word_zip_files')