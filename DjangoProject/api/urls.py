from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('getCompletedDisciplineView/<int:idStudent>/<int:idDiscipline>/<str:mark>', views.GetCompletedDisciplineView.as_view(), name="get"),
    path('setCompletedDisciplineView/<int:idStudent>/<int:idDiscipline>/<str:mark>', views.SetComletedDisciplineView.as_view(), name="set"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]

