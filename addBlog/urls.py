from django.urls import path
from .views import add_blog_page

urlpatterns = [
    path('' , add_blog_page , name = "add_blog_page"),
    
]
