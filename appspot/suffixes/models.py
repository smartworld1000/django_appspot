from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Suffix(models.Model):
	id = models.AutoField(primary_key=True)
	suffix = models.CharField(verbose_name=_('Suffix'), max_length=100, blank=False, null=False)