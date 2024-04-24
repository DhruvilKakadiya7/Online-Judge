from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from register.models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['country','university_name','profile_image']
        
        labels = {
            'country': 'Country',
            'university_name': 'University',
            'profile_image': 'Profile Image',
            
        }