from django.urls import path
from .views import blog_page , blog_details , blog_likes , blog_dislikes

urlpatterns = [
    path('' , blog_page , name = "blog_page"),
    path('<int:id>' , blog_details , name = "blog_details"),
    # path('<uuid:id>/likes',blog_likes, name="blog_likes")
    path('blog/<int:id>/likes/', blog_likes, name='blog_likes'),
    path('blog/<int:id>/dislikes/', blog_dislikes, name='blog_dislikes')

]
