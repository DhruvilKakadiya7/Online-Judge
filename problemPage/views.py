from django.shortcuts import render
from django.http import HttpResponse
from addProblem.models import Problem , TestCase
from .forms import SubmissionForm
from django.template import loader
from .models import Submission , TestcaseResult
from .config import *
from .cpp_compiler import run_cpp_code
import os

def readFile(file) :
    content = ""
    with open(file , "r") as file :
        for line in file.readlines() :
            content += line
    return content

def matchOutput(file1 , file2) :
    str1 = ""
    str2 = ""
    with open(file1 , "r") as file :
        for line in file.readlines() :
            str1 += line
    with open(file2 , "r") as file :
        for line in file.readlines() :
            str2 += line
    return str1 == str2

def getSourceCode(submission) :
    source_code_file_path = BASE_DIR + str(submission.source_file)
    source_code = []
    with open(source_code_file_path , "r") as file : 
        line_number = 1
        for line in file.readlines() :
            source_code.append(str(line_number).rjust(4) + "|  " + line.strip('\n\n'))
            line_number += 1
    return source_code

def getCompilationError(submission) :
    error_file_path = os.path.join(BASE_DIR , "error_tc\\error_" + str(submission.id) + ".txt")
    error_text = ""
    with open(error_file_path , "r") as file : 
        for line in file.readlines() :
            error_text += line.replace(BASE_DIR + "source_codes/", "")
    return error_text
    
    
def testcase(request , submission_id , testcase_id) :
    submission = Submission.objects.get(pk = submission_id)
    problem = Problem.objects.get(pk = submission.problem_id)
    testcase_results = submission.testcases_result.filter(tc_id = testcase_id).get()
    testcase = TestCase.objects.get(pk = testcase_id)
    print("hope : " ,  submission_id , testcase_id)
    return render(request , "testcase.html" , {
        "input" : testcase.input_text,
        "output" : testcase.output_text,
        "user_output" : testcase_results.user_output,
        "tc_no" : testcase.tc_id,
        "verdict" : testcase_results.verdict,
        "problem" : problem,
        "submission_id" : submission.id
    })

def submission(request , id) :
    submission = Submission.objects.get(pk = id)
    problem = Problem.objects.get(pk = submission.problem_id)
    testcase_results = submission.testcases_result.all()
    return render(request , "submission.html" , {'submission' : submission , 'source_code' : getSourceCode(submission) ,'testcase_results' : testcase_results , 'problem' : problem})

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
        form = SubmissionForm(request.POST , request.FILES)
        if form.is_valid() :
            instance = form.save()
            submission_id = instance.id
            submission = Submission.objects.filter(id = submission_id).get()
            source_code_file_path = BASE_DIR + str(submission.source_file)
            
            
            for testcase in Problem.objects.filter(id = id).get().testcases.all() :
                input_file_path = os.path.join(BASE_DIR , "input_tc\\" + str(id) + "\\" + "input_" + str(testcase.tc_id))
                output_file_path = os.path.join(BASE_DIR + "user_output_tc\\" + "output_" + str(submission_id) + "_" + str(testcase.tc_id) + ".txt")
                error_file_path = os.path.join(BASE_DIR , "error_tc\\error_" + str(submission_id) + "_" + str(testcase.tc_id) + ".txt")
                
                correct_output_path = os.path.join(BASE_DIR , "output_tc\\" + str(id) + "\\" + "output_" + str(testcase.tc_id))
                
                response = run_cpp_code(input_file = input_file_path , output_file = output_file_path , error_file = error_file_path , source_code = source_code_file_path)
                
                if response == ACCEPTED :
                    isCorrect = matchOutput(output_file_path , correct_output_path)
                    if not isCorrect :
                        response = WRONG_ANSWER
                        
                testcaseResult = TestcaseResult(
                    tc_id = testcase.id,
                    verdict = getMessage(response),
                    user_output = readFile(output_file_path),
                    problem_tc_id = testcase.tc_id
                )
                
                if response == COMPILATION_ERROR :
                    testcaseResult.details = getCompilationError(error_file_path)
                    
                testcaseResult.save()
                
                submission.testcases_result.add(testcaseResult)
                print("tc : " , testcase.tc_id , getMessage(response))
                
            
            
                
            submission_instance = Submission.objects.get(pk = submission_id)
            submission_instance.verdict = getMessage(response)      
            submission_instance.save()
            
            submissions = Submission.objects.filter(problem_id = id).order_by('submission_time').reverse()[:10] # add user id as well later on             
            problem = Problem.objects.filter(id = id).get()
            return render(request , "problem_details.html" ,
                        {'problem' : problem , 
                        'testcases' : problem.testcases.all(),
                        'submission_form' : SubmissionForm(),
                        'submissions' : submissions,
                        'verdict' : getMessage(response)
                        })
            
    submissions = Submission.objects.filter(problem_id = id).order_by('submission_time').reverse()[:10] # add user id as well later on             
    problem = Problem.objects.filter(id = id).get()
    return render(request , "problem_details.html" ,
                  {'problem' : problem , 
                   'testcases' : problem.testcases.all(),
                   'submission_form' : SubmissionForm(),
                   'submissions' : submissions
                   })
