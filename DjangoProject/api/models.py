from django.db import models

# Create your models here.
class CompletedDiscipline:
    def __init__(self, idStudent, idDiscipline, mark):
        self.idStudent = idStudent
        self.idDiscipline = idDiscipline
        self.mark = mark
