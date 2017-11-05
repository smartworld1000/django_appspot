from generic_scaffold import CrudManager
from . import models

class Case_typeCrudManager(CrudManager):
    model = models.Case_type
    prefix = 'case_types'