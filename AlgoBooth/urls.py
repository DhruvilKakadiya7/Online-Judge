from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/' , include('register.urls')),
    path('problem/' , include('problemPage.urls')),
    path('add_problem/' , include('addProblem.urls')),
    path('' , include('dashboard.urls'))
]
