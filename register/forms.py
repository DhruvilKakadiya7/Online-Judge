# from django import forms
# from .models import User

# class UserForm(forms.ModelForm) :
#     class Meta : 
#         model = User
#         fields = "__all__"
#         widgets = {
#             'password': forms.PasswordInput()
#         }
        
        
# class LoginForm(forms.ModelForm) : 
#     class Meta : 
#         model = User 
#         fields = ['user_name' , 'password']
#         widgets = {
#             'password': forms.PasswordInput()
#         }
        
        
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','first_name','last_name')

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        
