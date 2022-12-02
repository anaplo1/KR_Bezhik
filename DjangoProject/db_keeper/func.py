from .models import *
from django.db import connection
import sqlite3

#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 - Токен для гита


#  «Создание, хранение и обработка данных о количестве изученных студентом дисциплин»


def addStudent(name, surname, course, group):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute('INSERT INTO student ("name", "surname", "course", "group") VALUES (?,?,?,?) RETURNING *', (name, surname, course, group))
    row = cur.fetchone()

    cur.close()
    con.commit()

    return dict(row)
    # student = Student(name
    # =name, surname=surname, course=course, group=group)
    # student.save()
    # return student


def getStudent(name, surname, course, group):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('''SELECT * FROM student WHERE "name" LIKE ? AND "surname" LIKE ? AND "course" LIKE ? AND "group" LIKE ? ''', (f"%{name}%", f"%{surname}%", f"%{course}%", f"%{group}%"))
    row = cur.fetchall()

    cur.close()
    con.commit()

    row = [dict(i) for i in row]
    print(row)
    return row
    # student = Student.objects.filter(name__icontains=name) & Student.objects.filter(surname__icontains=surname) & \
    #         Student.objects.filter(course__icontains=course) & Student.objects.filter(group__icontains=group)
    # return student


def addDiscipline(title, description):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute('INSERT INTO discipline ("title", "description") VALUES (?,?) RETURNING *',
                (title, description))
    row = cur.fetchone()

    cur.close()
    con.commit()

    return dict(row)
    # discipline = Discipline(title=title, description=description)
    # discipline.save()
    # return discipline


def getDiscipline(title, description):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(
        '''SELECT * FROM discipline WHERE "title" LIKE ? AND "description" LIKE ? ''',
        (f"%{title}%", f"%{description}%"))
    row = cur.fetchall()

    cur.close()
    con.commit()

    row = [dict(i) for i in row]
    print(row)
    return row
    # discipline = Discipline.objects.filter(title__icontains=title) & \
    #             Discipline.objects.filter(description__icontains=description)
    # return discipline


def addCompletedDiscipline(idStudent, idDiscipline, mark):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute('INSERT INTO completeddiscipline ("idStudent", "idDiscipline", "mark") VALUES (?,?,?) RETURNING *',
                (idStudent, idDiscipline, mark))
    row = cur.fetchone()

    cur.close()
    con.commit()

    return dict(row)
    # completedDiscipline = CompletedDiscipline(idStudent=idStudent, idDiscipline=idDiscipline, mark=mark)
    # completedDiscipline.save()
    # return completedDiscipline


def getCompletedDiscipline(idStudent, idDiscipline, mark):
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(
        '''SELECT * FROM completeddiscipline WHERE "idStudent" LIKE ? AND "idDiscipline" LIKE ? AND "mark" LIKE ? ''',
        (f"%{idStudent}%", f"%{idDiscipline}%", f"%{mark}%"))
    row = cur.fetchall()

    cur.close()
    con.commit()

    row = [dict(i) for i in row]
    print(row)
    return row
    # completedDiscipline = CompletedDiscipline.objects.filter(idStudent__icontains=idStudent) & \
    #                     CompletedDiscipline.objects.filter(idDiscipline__icontains=idDiscipline) & \
    #                     CompletedDiscipline.objects.filter(mark__icontains=mark)
    # return completedDiscipline


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]