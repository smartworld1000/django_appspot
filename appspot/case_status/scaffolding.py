from generic_scaffold import CrudManager
from . import models

class Case_statusCrudManager(CrudManager):
    model = models.Case_status
    prefix = 'case_status'