from django.shortcuts import render
from django.http import HttpResponse
from addProblem.models import Problem , TestCase
from .forms import SubmissionForm

def problem_page(request) :
    if request.method == "POST" :
        rating_from = request.POST['rating_from']
        rating_to = request.POST['rating_to']
        
        solved_from = request.POST['solved_from']
        solved_to = request.POST['solved_to']
        
        print(rating_from , rating_to)
        problems = Problem.objects.filter(rating__range=(rating_from , rating_to)).values('id' , 'name' , 'rating')
        print(problems)
        context = {
            'problems' : problems,
            'rating_from' : rating_from,
            'rating_to' : rating_to,
            'solved_from' : solved_from,
            'solved_to' : solved_to,
        }
        return render(request , "problem_page.html" , context=context)
    problems = Problem.objects.values('id' , 'name' , 'rating').order_by('added_date')
    return render(request , "problem_page.html" , {'problems': problems})

def problem_details(request , id) :
    if request.method == "POST" :
        print("requested --------------------------")
        form = SubmissionForm(request.POST , request.FILES)
        if form.is_valid() :
            form.save()
            print("done done done")
    problem = Problem.objects.filter(id = id).get()
    return render(request , "problem_details.html" ,
                  {'problem' : problem , 
                   'testcases' : problem.testcases.all(),
                   'submission_form' : SubmissionForm()
                   })
