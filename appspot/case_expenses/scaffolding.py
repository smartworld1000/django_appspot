from generic_scaffold import CrudManager
from . import models

class Case_expenseCrudManager(CrudManager):
    model = models.Case_expense
    prefix = 'case_expenses'