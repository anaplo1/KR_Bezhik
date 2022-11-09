from django.contrib import admin
from django.urls import path
from db_worker import views

urlpatterns = [
    path('getStudent', views.queryGetStudent),
    path('addStudent', views.querySetStudent),
    path('getDiscipline', views.queryGetDiscipline),
    path('addDiscipline', views.querySetDiscipline),
    path('getCompletedDiscipline', views.queryGetCompletedDiscipline),
    path('setCompletedDiscipline', views.querySetCompletedDiscipline)
]
