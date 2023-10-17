from django.urls import path
from .views import problem_page , problem_details

urlpatterns = [
    path('' , problem_page , name = "problem_page"),
    path('<int:id>' , problem_details , name = "problem_details")
]
