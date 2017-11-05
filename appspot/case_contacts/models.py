from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case
from appspot.person.models import Person
from generic_scaffold import get_url_names
from django.core.urlresolvers import reverse

# Create your models here.
class Case_contact(models.Model):
	id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative case'), related_name='case_contacts')
	client = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='case_contacts')

	def __unicode__(self):
		return self.label

	def get_absolute_url(self):
		return reverse(get_url_names(prefix='case_contacts')['detail'], args=(self.id,))

	class Meta:
		verbose_name = _('case_contact')
		verbose_name_plural = _('case_contacts')