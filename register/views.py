# from django.shortcuts import render, redirect
# from .models import User
# from .forms import UserForm, LoginForm

# def register(request) :
#     if request.method == "POST" :
#         form = UserForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = User(
#                 user_name = data['user_name'],
#                 first_name = data['first_name'],
#                 last_name = data['last_name'],
#                 email = data['email'],
#                 password = data['password']
#             )
#             user.save()
#         return redirect('login')
#     return render(request , "register.html" , {'form' : UserForm()})

# def login(request) :
#     if request.method == "POST" :
#         form = LoginForm(request.POST)
#         if form.is_valid() :
#             data = form.cleaned_data
#             user_count = User.objects.filter(user_name = data['user_name']).count()
#             if user_count > 0 :
#                 password = User.objects.filter(user_name = data['user_name']).values('password')
#                 if data['password'] != password[0]['password'] :
#                     print("correct : " , password[0]['password'])
#                     info = "Wrong Password"
#                     return render(request , "login.html" , context = {'form' : LoginForm() , 'info' : info})
#                 return redirect('dashboard')
#             else :
#                 info = "User Not Exist"
#                 return render(request , "login.html" , context = {'form' : LoginForm() , 'info' : info})
#     return render(request , "login.html" , {'form' : LoginForm()})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page after login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})
