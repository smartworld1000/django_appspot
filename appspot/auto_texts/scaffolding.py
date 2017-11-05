from generic_scaffold import CrudManager
from . import models

class Auto_textCrudManager(CrudManager):
    model = models.Auto_text
    prefix = 'auto_texts'