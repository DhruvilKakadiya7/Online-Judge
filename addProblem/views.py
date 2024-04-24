from django.shortcuts import render
from .models import TestCase , Problem 
from .forms import AddProblemForm
from datetime import datetime
import os

def writeFile(path , content) :
    with open(path , "w") as file :
        file.write(content.replace("\r" , ""))

def createDirectory(dir_path) :
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return
    else:
        os.mkdir(dir_path)
        

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
        
        print("id : " , problem.id)
        
        print(request.POST)
        
        tc_shown_id = 0
        
        for cnt in range(1 , 100) :
            input_name = "input" + str(cnt)
            output_name = "output" + str(cnt)
            show_name = "show" + str(cnt)
            show = False
            
            BASE_DIR = "G:\\SEM-7\\ADF\\FINAL PROJECT\\HOPE 2.0\\algobooth-adf\\media\\"
            createDirectory(os.path.join(BASE_DIR , "input_tc\\" + str(problem.id)))
            createDirectory(os.path.join(BASE_DIR , "output_tc\\" + str(problem.id)))
            input_file_path = os.path.join(BASE_DIR , "input_tc\\" + str(problem.id) + "\\" + "input_" + str(cnt))
            output_file_path = os.path.join(BASE_DIR , "output_tc\\" + str(problem.id) + "\\" + "output_" + str(cnt))
            
            if show_name in request.POST and request.POST[show_name] == 'on' :
                show = True
                tc_shown_id += 1
            if input_name not in request.POST :
                break
            
            writeFile(input_file_path , request.POST[input_name])
            writeFile(output_file_path , request.POST[output_name])
            
            testcase = TestCase(
                tc_id = cnt,
                show = show,
                tc_shown_id = tc_shown_id,
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
    