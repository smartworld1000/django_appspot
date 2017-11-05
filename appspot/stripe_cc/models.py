from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.person.models import Person

# Create your models here.
class stripe_cc(models.Model):
	id = models.AutoField(primary_key=True)
	client = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='credit_cards')
	stripe_customer_id = models.CharField(verbose_name=_('Stripe customer ID'), max_length=100, blank=False, null=False)
	cc_last_four = models.CharField(verbose_name=_('CC last four'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('stripe_cc')
		verbose_name_plural = _('stripe_ccs')