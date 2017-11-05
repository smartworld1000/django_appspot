from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.updates.models import Update

# Create your models here.
class Update_media(models.Model):
	id = models.AutoField(primary_key=True)
	case_update = models.ForeignKey(Update, blank=False, null=False, verbose_name=_('Update'), related_name='update_files')
	media = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	file_name = models.CharField(verbose_name=_('File name'), max_length=100, blank=False, null=False)
	mime = models.CharField(verbose_name=_('Mime'), max_length=100, blank=False, null=False)

	blob_size = models.IntegerField(verbose_name=_('Blob size'), unique=False, blank=False, null=False)

	class Meta:
		verbose_name = _('update media')
		verbose_name_plural = _('update medias')