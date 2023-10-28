from django.urls import path
from .views import dashboard, hope
urlpatterns = [
    path('' , dashboard , name = 'dashboard'),
    path('hope/' , hope , name = 'hope')
]
