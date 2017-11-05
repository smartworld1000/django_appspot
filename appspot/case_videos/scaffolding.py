from generic_scaffold import CrudManager
from . import models

class Case_videoCrudManager(CrudManager):
    model = models.Case_video
    prefix = 'case_videos'