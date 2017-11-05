from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.update_types.models import Update_type
from appspot.case_contacts.models import Case_contact

# Create your models here.
class update_option(models.Model):
	id = models.AutoField(primary_key=True)
	update_type = models.ForeignKey(Update_type, blank=False, null=False, verbose_name=_('Upadate type'), related_name='updates')
	contact = models.ForeignKey(Case_contact, blank=False, null=False, verbose_name=_('Case contact'), related_name='update_options')

	class Meta:
		verbose_name = _('update_option')
		verbose_name_plural = _('update_options')