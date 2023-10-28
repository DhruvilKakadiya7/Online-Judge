from django.db import models
from django.contrib import admin
# Create your models here.

class TestCase(models.Model) :
    tc_id = models.IntegerField()
    tc_shown_id = models.IntegerField(default = -1)
    input_text = models.TextField()
    output_text = models.TextField()
    show = models.BooleanField(default = True)
    
    class Meta : 
        db_table = "testcases"
    
class Problem(models.Model) :
    name = models.CharField(max_length = 100)
    rating = models.IntegerField()
    statement = models.TextField()
    input_description = models.TextField(null = True , blank = True)
    output_description = models.TextField(null = True , blank = True)
    testcases = models.ManyToManyField(TestCase)
    explanation = models.TextField(null = True , blank = True)
    added_date = models.DateTimeField(auto_now_add = True)
    
    class Meta: 
        db_table = "problems"
        
admin.site.register(Problem)