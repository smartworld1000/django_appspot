from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Prefix(models.Model):
	id = models.AutoField(primary_key=True)
	prefix = models.CharField(verbose_name=_('Prefix'), max_length=100, blank=False, null=False)