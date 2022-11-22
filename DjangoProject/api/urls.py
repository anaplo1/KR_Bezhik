from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('getCompletedDisciplineView/<int:idStudent>/<int:idDiscipline>/<str:mark>', views.CompletedDisciplineView.as_view()),
    path('setCompletedDisciplineView/<int:idStudent>/<int:idDiscipline>/<str:mark>', views.CompletedDisciplineView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]

