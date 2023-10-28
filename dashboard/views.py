from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
# Create your views here.
def dashboard(request) :
    return render(request , "dashboard.html")

def hope(request) :
    data = {
        "value" : "We are done now. Time : " + str(datetime.now().second)
    }
    return JsonResponse(data)