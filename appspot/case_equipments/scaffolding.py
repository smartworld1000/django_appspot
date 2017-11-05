from generic_scaffold import CrudManager
from . import models

class Case_equipmentCrudManager(CrudManager):
    model = models.Case_equipment
    prefix = 'case_equipments'