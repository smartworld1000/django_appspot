from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	email_address = models.EmailField(verbose_name=_('Email address'), max_length=254, unique=True)
	investigator_id = models.IntegerField(verbose_name=_('Investigator id'), unique=False, blank=True, null=True)
	name = models.CharField(verbose_name=_('Name'), max_length=100)

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')