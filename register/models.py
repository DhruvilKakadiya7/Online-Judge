from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    country = models.CharField(max_length=100,blank=True, null=True)
    university_name = models.CharField(max_length=100,blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True,default='profile_image/blank-profile-picture.png')
