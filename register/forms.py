from django import forms
from .models import User

class UserForm(forms.ModelForm) :
    class Meta : 
        model = User
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput()
        }
        
        
class LoginForm(forms.ModelForm) : 
    class Meta : 
        model = User 
        fields = ['user_name' , 'password']
        widgets = {
            'password': forms.PasswordInput()
        }