from django.urls import path
from .views import blog_page , blog_details , blog_likes , blog_dislikes, add_comment

urlpatterns = [
    path('' , blog_page , name = "blog_page"),
    path('<int:id>' , blog_details , name = "blog_details"),
    # path('<uuid:id>/likes',blog_likes, name="blog_likes")
    path('blog/<int:id>/likes/', blog_likes, name='blog_likes'),
    path('blog/<int:id>/dislikes/', blog_dislikes, name='blog_dislikes'),
    # path('add_comment/<int:id>/', add_comment, name='add_comment')

    # path('add_comment/<int:id>/', add_comment, name='add_comment'),
    # path('add_comment/<int:parent_comment_id>/', add_comment, name='add_reply'),
    # path('list_comments/', list_comments, name='list_comments'),
    
    path('add_comment/<int:blog_id>/', add_comment, name='add_comment'),  # URL pattern for top-level comments
    path('add_comment/<int:blog_id>/<int:comment_id>/', add_comment, name='add_comment'),  # URL pattern for replies
]



