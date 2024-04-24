from django.urls import path
from .views import problem_page , contribution , problem_details , download_file , submission , testcase , standing

urlpatterns = [
    path('' , problem_page , name = "problem_page"),
    path('standing' , standing , name = "standing_page"),
    path('contribution' , contribution , name = "contribution_page"),
    path('<int:id>' , problem_details , name = "problem_details"),
    path("submission/<int:id>" , submission , name = 'submission'),
    path("download_file/<int:problem_id>" , download_file , name = 'download_file'),
    path("submission/<int:submission_id>/<int:testcase_id>" , testcase , name = 'testcase')
]
