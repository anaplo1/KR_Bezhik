from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CompletedDiscipline
from .serializers import CompletedDisciplineSerializer
from db_keeper.func import getCompletedDiscipline, addCompletedDiscipline


class CompletedDisciplineView(APIView):


    def get(self, request, idStudent, idDiscipline, mark):

        a = getCompletedDiscipline(idStudent, idDiscipline, mark)
        print(a)
        a = (CompletedDisciplineSerializer(instance=st).data for st in a) if a is not None else []

        return Response(a)


    def set(self, request, idStudent, idDiscpline, mark):

        a = addCompletedDiscipline(idStudent, idDiscpline, mark)
        a.idStudent = CompletedDisciplineSerializer(instance=a.idStudent).data
        a.idDiscipline = CompletedDisciplineSerializer(instance=a.idDiscipline).data
        a.mark = CompletedDisciplineSerializer(instance=a.mark).data

        return Response(a)