from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from db_keeper.func import *

#  «Создание, хранение и обработка данных о количестве изученных студентом дисциплин»


def index(request):
    return HttpResponse("Hello")


def queryGetStudent(request):
    name = request.GET.get("name")
    surname = request.GET.get("surname")
    course = request.GET.get("course")
    group = request.GET.get("group")

    student = getStudent(name, surname, course, group)

    print(student)
    return HttpResponse((f"ID студента: {obj['id']} - Имя: {obj['name']}, Фамилия: {obj['surname']}, Курс: {obj['course']}, Группа: {obj['group']}<br>" for obj in student) if len(student) else f"Студент не существует в базе")


def querySetStudent(request):
    name = request.GET.get("name")
    surname = request.GET.get("surname")
    course = request.GET.get("course")
    group = request.GET.get("group")

    student = addStudent(name, surname, course, group)
    return HttpResponse(
        (f"Студент с данными: - ID студента: {student['id']} - Имя: {student['name']}, Фамилия: {student['surname']}, Курс: {student['course']}, Группа: {student['group']}<br> Успешно внесен!"))


def queryGetDiscipline(request):
    title = request.GET.get("title")
    description = request.GET.get("description")

    discipline = getDiscipline(title, description)

    return HttpResponse((f"Дисциплина с данными: - ID дисциплины: {obj['id']}, Название: {obj['title']}, Описание: {obj['description']}<br>" for obj in discipline) if len(discipline) else f"Дисциплина не существует в базе")


def querySetDiscipline(request):
    title = request.GET.get("title")
    description = request.GET.get("description")

    discipline = addDiscipline(title, description)

    return HttpResponse(f"Дисциплина с данными: - ID дисциплины: {discipline['id']}, Название: {discipline['title']}, Описание: {discipline['description']}<br>Успешно внесена!")


def queryGetCompletedDiscipline(request):
    idStudent = request.GET.get("idStudent")
    idDiscipline = request.GET.get("idDiscipline")
    mark = request.GET.get("mark")

    completedDiscipline = getCompletedDiscipline(idStudent, idDiscipline, mark)

    return HttpResponse((f"Закрытая дисциплина: - ID сдачи дисциплины: {obj['id']}, ID студента {obj['idStudent']}, ID предмета: {obj['idDiscipline']}, Оценка: {obj['mark']}<br>" for obj in completedDiscipline) if len(completedDiscipline) else "Данной дисциплины среди сданных нет")


def querySetCompletedDiscipline(request):
    idStudent = request.GET.get("idStudent")
    idDiscipline = request.GET.get("idDiscipline")
    mark = request.GET.get("mark")

    idStudent = int(idStudent)
    print(type(idStudent), idDiscipline)

    completedDiscipline = addCompletedDiscipline(idStudent, idDiscipline, mark)

    return HttpResponse(
            f"Закрытая дисциплина: - ID сдачи дисциплины: {completedDiscipline['id']}, ID студента {completedDiscipline['idStudent']}, ID предмета: {completedDiscipline['idDiscipline']}, Оценка: {completedDiscipline['mark']}<br>Успешно добавлена!")
