from django.urls import path
from .views import profile_page, my_submissions, profile_setting , global_submissions

urlpatterns = [
    path("" , profile_page , name = 'profile_page'),
    path("<str:id>/my_submissions/" , my_submissions , name = 'my_submissions'),
    path("global_submissions/" , global_submissions , name = 'global_submissions'),
    path('profile_setting/', profile_setting, name='profile_setting'),
]


