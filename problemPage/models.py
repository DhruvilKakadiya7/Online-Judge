from django.db import models

# Create your models here.

class TestCases(models.Model) :
    input_text = models.TextField()
    output_text = models.TextField()
    
class Problem(models.Model) :
    name = models.CharField(max_length = 100)
    statement = models.TextField()
    input_description = models.TextField()
    output_description = models.TextField()
    testcases = models.ForeignKey(TestCases , on_delete = models.CASCADE)
    explanation = models.TextField()
    
