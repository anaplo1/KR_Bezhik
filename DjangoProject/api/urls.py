from django.urls import path
from . import views

urlpatterns = [
    path('getCompletedDisciplineView/<int:idStudent>/<int:idDiscipline>/<str:mark>', views.CompletedDisciplineView.as_view()),
    path('setCompletedDisciplineView/<int:idStudent>/<int:idDiscipline>/<str:mark>', views.CompletedDisciplineView.as_view())
]