from django.shortcuts import render
from .models import TestCase , Problem 
from .forms import AddProblemForm
from datetime import datetime

def add_problem_page(request) :
    
    if request.method == "POST" :
        
        # <QueryDict: {'csrfmiddlewaretoken': ['MiQWbtMamgpF212DYg4yacyHGWY3qYCNGZSXTzX7l8E2LAL4KFSFD88LdT9opSNy'], 'name': ['gfdghf'], 'rating': ['344545'], 'statement': ['gfdgfdgfdg'], 'input_description': ['gfdgfd'], 'output_description': ['gfdgfdg'], 'input1': ['gfd'], 'output1': ['fdgfdgfdg'], 'input2': ['fdgfg'], 'output2': ['dfgfdg'], 'explanation': ['fdgfdgfd']}>
        print(request.POST)
        print("KEYS :" , request.POST.__dict__.keys())
        name = request.POST['name']
        rating = request.POST['rating']
        statement = request.POST['statement']
        
        print("statement : " , statement)
        input_desc = request.POST['input_description']
        output_desc = request.POST['output_description']
        time = datetime.now()
        explanation = request.POST['explanation']
        
        problem = Problem(
            name = name,
            rating = rating,
            statement = statement,
            input_description = input_desc,
            output_description = output_desc,
            explanation = explanation
        )
        problem.save()
        
        
        
        for cnt in range(1 , 100) :
            input_name = "input" + str(cnt)
            output_name = "output" + str(cnt)
            if input_name not in request.POST :
                break
            
            testcase = TestCase(
                tc_id = cnt,
                input_text = request.POST[input_name],
                output_text = request.POST[output_name]
            )
            
            testcase.save()
            problem.testcases.add(testcase)
            print("test case success:" , cnt)
    
    return render(request , "add_problem_page.html" , {'form' : AddProblemForm()})


def add_testcase(request) :
    print("done")
    return render(request , "add_problem_page.html" , {'form' : AddProblemForm()})
    