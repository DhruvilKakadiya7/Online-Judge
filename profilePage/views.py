from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile_page(request) :
    return render(request , "profile_page.html")
    