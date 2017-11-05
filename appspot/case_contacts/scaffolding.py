from generic_scaffold import CrudManager
from . import models

class Case_contactCrudManager(CrudManager):
    model = models.Case_contact
    prefix = 'case_contacts'