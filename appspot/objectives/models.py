from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case

# Create your models here.
class objective(models.Model):
	id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative case'), related_name='objectives')
	number = models.IntegerField(verbose_name=_('Number'), unique=False, blank=False, null=False)
	text = models.CharField(verbose_name=_('Text'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('objective')
		verbose_name_plural = _('objectives')