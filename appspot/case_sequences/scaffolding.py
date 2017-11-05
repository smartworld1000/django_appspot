from generic_scaffold import CrudManager
from . import models

class Case_sequenceCrudManager(CrudManager):
    model = models.Case_sequence
    prefix = 'case_sequences'