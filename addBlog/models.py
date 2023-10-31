from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to="media/blog_image")
    added_date = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # comments = models.TextField()
    
    class Meta: 
        db_table = "blog"
        
