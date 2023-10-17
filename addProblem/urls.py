from django.urls import path
from .views import add_problem_page , add_testcase

urlpatterns = [
    path('' , add_problem_page , name = "add_problem_page"),
    path('/add' , add_testcase , name = "add_testcase")
]
