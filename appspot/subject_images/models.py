from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person

# Create your models here.
class subject_images(models.Model):
	id = models.AutoField(primary_key=True)
	person = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='subject_images')
	picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	file_name = models.CharField(verbose_name=_('File name'), max_length=100, blank=False, null=False)
	mime = models.CharField(verbose_name=_('Mime'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = "subject_image"
		verbose_name_plural = "subject_images"