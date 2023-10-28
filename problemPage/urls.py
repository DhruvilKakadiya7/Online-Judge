from django.urls import path
from .views import problem_page , problem_details , submission , testcase

urlpatterns = [
    path('' , problem_page , name = "problem_page"),
    path('<int:id>' , problem_details , name = "problem_details"),
    path("submission/<int:id>" , submission , name = 'submission'),
    path("submission/<int:submission_id>/<int:testcase_id>" , testcase , name = 'testcase')
]
