from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, LoginForm

def register(request) :
    if request.method == "POST" :
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(
                user_name = data['user_name'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = data['password']
            )
            user.save()
        return redirect('login')
    return render(request , "register.html" , {'form' : UserForm()})

def login(request) :
    if request.method == "POST" :
        form = LoginForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            user_count = User.objects.filter(user_name = data['user_name']).count()
            if user_count > 0 :
                password = User.objects.filter(user_name = data['user_name']).values('password')
                if data['password'] != password[0]['password'] :
                    print("correct : " , password[0]['password'])
                    info = "Wrong Password"
                    return render(request , "login.html" , context = {'form' : LoginForm() , 'info' : info})
                return redirect('dashboard')
            else :
                info = "User Not Exist"
                return render(request , "login.html" , context = {'form' : LoginForm() , 'info' : info})
    return render(request , "login.html" , {'form' : LoginForm()})