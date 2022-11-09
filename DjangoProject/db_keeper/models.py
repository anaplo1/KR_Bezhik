from django.db import models


class Student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    course = models.TextField()
    group = models.TextField()


class Discipline(models.Model):
    title = models.TextField()
    description = models.TextField()


class CompletedDiscipline(models.Model):
    idStudent = models.IntegerField()
    idDiscipline = models.IntegerField()
    mark = models.TextField()
