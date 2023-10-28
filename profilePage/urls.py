from django.urls import path
from .views import profile_page, my_submissions

urlpatterns = [
    path("" , profile_page , name = 'profile_page'),
    path("<str:id>/my_submissions/" , my_submissions , name = 'my_submissions'),
]
