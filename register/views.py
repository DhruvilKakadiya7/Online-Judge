

from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm


def error_message_from_html(temp) :
    html_error = str(temp)
    soup = BeautifulSoup(html_error, 'html.parser')
    error_text = soup.find('li')
    
    error_info = ""
    first = False
    for each in error_text :
        if not first :
            first = True
        else :
            error_info = each.text
    
    return error_info
                    
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page after registration
        else :
            return render(request , 'register.html' , {'form' : form , 'info' : error_message_from_html(form.errors)})
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
        else :
            return render(request , 'login.html' , {
                'form' : form,
                'info' : error_message_from_html(form.errors)
            })
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or any other desired URL after logout




