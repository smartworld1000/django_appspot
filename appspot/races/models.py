from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Race(models.Model):
	id = models.AutoField(primary_key=True)
	race = models.CharField(verbose_name=_('Race'), max_length=100, blank=False, null=False)