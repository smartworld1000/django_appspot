from generic_scaffold import CrudManager
from . import models

class CompanyCrudManager(CrudManager):
    model = models.Company
    prefix = 'companies'