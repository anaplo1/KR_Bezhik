from .models import *
from django.db import connection


#  «Создание, хранение и обработка данных о количестве изученных студентом дисциплин»


def addStudent(name, surname, course, group):
    student = Student(name=name, surname=surname, course=course, group=group)
    student.save()
    return student


def getStudent(name, surname, course, group):
    # try:
    student = Student.objects.filter(name__icontains=name) & Student.objects.filter(surname__icontains=surname) & \
            Student.objects.filter(course__icontains=course) & Student.objects.filter(group__icontains=group)
    # except Student.DoesNotExist:
    #     student = None
    return student


def addDiscipline(title, description):
    discipline = Discipline(title=title, description=description)
    discipline.save()
    return discipline


def getDiscipline(title, description):
    # try:
    discipline = Discipline.objects.filter(title__icontains=title) & \
                Discipline.objects.filter(description__icontains=description)
    # except Discipline.DoesNotExist:
    #     discipline = None
    return discipline


def addCompletedDiscipline(idStudent, idDiscipline, mark):
    completedDiscipline = CompletedDiscipline(idStudent=idStudent, idDiscipline=idDiscipline, mark=mark)
    completedDiscipline.save()
    return completedDiscipline


def getCompletedDiscipline(idStudent, idDiscipline, mark):
    # try:
    completedDiscipline = CompletedDiscipline.objects.filter(idStudent__icontains=idStudent) & \
                        CompletedDiscipline.objects.filter(idDiscipline__icontains=idDiscipline) & \
                        CompletedDiscipline.objects.filter(mark__icontains=mark)
    # except CompletedDiscipline.DoesNotExist:
    #     completedDiscipline = None
    return completedDiscipline


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]