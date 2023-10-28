from django.db import models
from django.contrib import admin

LANG_CHOICES = (
    ('c++', 'cpp'),
    ('python', 'Python'),
    ('java', 'Java'),
)

class TestcaseResult(models.Model) :
    tc_id = models.IntegerField()
    problem_tc_id = models.IntegerField(default = -1)
    verdict = models.CharField(max_length = 50)
    details = models.TextField(default = "")
    user_output = models.TextField(default = "")
    
class Submission(models.Model) :
    problem_id = models.IntegerField()
    user_id = models.IntegerField()
    submission_time = models.DateTimeField(auto_now_add = True)
    language = models.CharField(max_length = 50 , choices = LANG_CHOICES , default = 'c++')
    verdict = models.CharField(max_length = 50 , null = True)    
    source_file = models.FileField(upload_to = 'source_codes/' , null = True)
    testcases_result = models.ManyToManyField(TestcaseResult , default = None)
    
admin.site.register(Submission)