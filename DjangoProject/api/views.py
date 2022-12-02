from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CompletedDiscipline
from .serializers import CompletedDisciplineSerializer
from db_keeper.func import getCompletedDiscipline, addCompletedDiscipline
from drf_spectacular.utils import extend_schema


class GetCompletedDisciplineView(APIView):
    @extend_schema(request=CompletedDisciplineSerializer, responses=CompletedDisciplineSerializer)

    def get(self, request, idStudent, idDiscipline, mark):

        a = getCompletedDiscipline(idStudent, idDiscipline, mark)
        print(a)
        a = (CompletedDisciplineSerializer(instance=st).data for st in a) if a is not None else []

        return Response(a)


class SetComletedDisciplineView(APIView):
    @extend_schema(request=CompletedDisciplineSerializer, responses=CompletedDisciplineSerializer)

    def get(self, request, idStudent, idDiscipline, mark):
        a = addCompletedDiscipline(idStudent, idDiscipline, mark)

        return Response(a)