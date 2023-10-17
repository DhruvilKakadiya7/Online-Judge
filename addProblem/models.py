from django.db import models

# Create your models here.

class TestCase(models.Model) :
    tc_id = models.IntegerField()
    input_text = models.TextField()
    output_text = models.TextField()
    
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