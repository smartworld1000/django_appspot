from generic_scaffold import CrudManager
from . import models

class AssignmentCrudManager(CrudManager):
    model = models.Assignment
    prefix = 'assignments'