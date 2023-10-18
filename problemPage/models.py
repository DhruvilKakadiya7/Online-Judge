from django.db import models

LANG_CHOICES = (
    ('c++', 'cpp'),
    ('python', 'Python'),
    ('java', 'Java'),
)

class Submission(models.Model) :
    problem_id = models.IntegerField()
    user_id = models.IntegerField()
    submission_time = models.DateTimeField(auto_now_add = True)
    language = models.CharField(max_length = 50 , choices = LANG_CHOICES , default = 'c++')
    verdict = models.CharField(max_length = 50 , null = True)    
    source_file = models.FileField(upload_to = 'source_codes/' , null = True)