from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person

# Create your models here.
EMAIL_TYPE = (
	('HOME', _('Home')),
	('WORK', _('Work')),
	('OTHER', _('Other')),
)

class Email(models.Model):
	id = models.AutoField(primary_key=True) 
	person = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='email_addresses')
	email_type = models.CharField(verbose_name=_('Email type'),  max_length=100, choices=EMAIL_TYPE)
	email_address = models.EmailField(help_text=_(''))
	email_label = models.CharField(verbose_name=_('Email label'), max_length=100, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(help_text=_(''))

	class Meta:
		verbose_name = _('email')
		verbose_name_plural = _('emails')