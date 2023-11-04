from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(models.Model) :
#     user_name = models.CharField(max_length = 50)
#     first_name = models.CharField(max_length = 50)
#     last_name = models.CharField(max_length = 50)
#     email = models.EmailField()
#     password = models.CharField(max_length = 50)
    



class CustomUser(AbstractUser):
    # Add custom fields here if needed
    pass
