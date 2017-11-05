from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
GENDER = (
	('male', _('Male')),
	('female', _('Female')),
)

class Gender(models.Model):
	id = models.AutoField(primary_key=True)
	gender = models.CharField(verbose_name=_('Gender'), max_length=100, choices=GENDER)

	class Meta:
		verbose_name = _('gender')
		verbose_name_plural = _('genders')