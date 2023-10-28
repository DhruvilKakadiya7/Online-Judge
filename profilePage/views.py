from django.shortcuts import render
from django.http import HttpResponse
from problemPage.models import Submission

# Create your views here.
def profile_page(request) :
    return render(request , "profile_page.html")


def my_submissions(request , id) :
    submissions = Submission.objects.filter(user_id = id).order_by('submission_time').reverse()
    for each in submissions : 
        print(each)
    return render(request , "my_submissions.html" , {'submissions' : submissions})