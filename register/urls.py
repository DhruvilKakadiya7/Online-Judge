from django.urls import path
from .views import user_register , user_login, custom_logout

urlpatterns = [
    path("signup/" , user_register , name = 'register'),
    path("login/" , user_login , name = 'login')  ,
    path('logout/', custom_logout, name='logout'), 
    

]
