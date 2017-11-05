from generic_scaffold import CrudManager
from . import models

class Auto_text_fieldCrudManager(CrudManager):
    model = models.Auto_text_field
    prefix = 'auto_text_fields'