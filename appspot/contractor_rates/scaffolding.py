from generic_scaffold import CrudManager
from . import models

class Contractor_rateCrudManager(CrudManager):
    model = models.Contractor_rate
    prefix = 'contractor_rates'