from generic_scaffold import CrudManager
from . import models

class AddressCrudManager(CrudManager):
    model = models.Address
    prefix = 'addresses'