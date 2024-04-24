from django.shortcuts import render
from django.http import HttpResponse
from addProblem.models import Problem , TestCase
from .forms import SubmissionForm
from django.template import loader
from .models import Submission , TestcaseResult
from .config import *
from .cpp_compiler import run_cpp_code
from register.models import CustomUser
from django.db.models import Count
from .pdfgen import create_problem_pdf
from addBlog.models import Blog
from blogPage.models import Like, Dislike
from django.contrib.auth.decorators import login_required
import os

def readFile(file) :
    content = ""
    try : 
        with open(file , "r") as file :
            for line in file.readlines() :
                content += line
    except :
        content = "file not found."
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

def getCompilationError(submission , tc_id) :
    error_file_path = os.path.join(BASE_DIR , "error_tc\\error_" + str(submission.id) + "_" + str(tc_id) + ".txt")
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
            base_source_code = source_code_file_path
            
            correct_sol = True
            fre = {
                ACCEPTED : 0,
                COMPILATION_ERROR : 0,
                RUNTIME_ERROR : 0,
                TIME_LIMIT_EXCEEDED : 0,
                MEMORY_LIMIT_EXCEEDED : 0,
                WRONG_ANSWER : 0,
            }
            
            for testcase in Problem.objects.filter(id = id).get().testcases.all() :
                input_file_path = os.path.join(BASE_DIR , "input_tc\\" + str(id) + "\\" + "input_" + str(testcase.tc_id))
                output_file_path = os.path.join(BASE_DIR + "user_output_tc\\" + "output_" + str(submission_id) + "_" + str(testcase.tc_id) + ".txt")
                error_file_path = os.path.join(BASE_DIR , "error_tc\\error_" + str(submission_id) + "_" + str(testcase.tc_id) + ".txt")
                
                correct_output_path = os.path.join(BASE_DIR , "output_tc\\" + str(id) + "\\" + "output_" + str(testcase.tc_id))
                
                response = run_cpp_code(input_file = input_file_path , output_file = output_file_path , error_file = error_file_path , source_code = source_code_file_path)
                
                print(response , getMessage(response));
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
                
                fre[response] += 1
                
                if response != ACCEPTED :
                    correct_sol = False
                    
                if response == COMPILATION_ERROR :
                    testcaseResult.details = getCompilationError(submission , testcase.tc_id)
                    
                if response == RUNTIME_ERROR :
                    testcaseResult.details = "Run time error occured."
                
                if response == WRONG_ANSWER :
                    testcaseResult.details = "Your answer is not matching with correct answer."
                
                if response == ACCEPTED :
                    testcaseResult.details = "Correct !!"
                    
                if response == TIME_LIMIT_EXCEEDED :
                    testcaseResult.details = "Your code taking too long time to execute the input."
                    new_source_code_path = BASE_DIR + "temp_tle_codes\\" + str(submission_id) + "_" + str(testcase.tc_id) + ".cpp"
                    
                    with open(new_source_code_path , "w") as file, open(base_source_code , "r") as input_file : 
                        for line in input_file.readlines() :
                            file.write(line)
                            
                    source_code_file_path = new_source_code_path
                    
                testcaseResult.save()
                
                submission.testcases_result.add(testcaseResult)
                print("tc : " , testcase.tc_id , getMessage(response))
                
            
            
                
            submission_instance = Submission.objects.get(pk = submission_id)
            submission_instance.user_id = request.user.id
            
            if correct_sol :
                submission_instance.verdict = getMessage(ACCEPTED)
            else :
                maxi = 0
                for key in fre.keys() :
                    if key == ACCEPTED : continue
                    maxi = max(maxi , fre[key])
                    
                for key in fre.keys() :
                    if key == ACCEPTED : continue
                    if fre[key] == maxi :
                        submission_instance.verdict = getMessage(key)
                        break
                          
            submission_instance.save()
            print("user id : " , request.user.id)
            
            
            
            submissions = Submission.objects.filter(problem_id = id , user_id = request.user.id).order_by('submission_time').reverse()[:10] # add user id as well later on             
            problem = Problem.objects.filter(id = id).get()
            return render(request , "problem_details.html" ,
                        {'problem' : problem , 
                        'testcases' : problem.testcases.all(),
                        'submission_form' : SubmissionForm(),
                        'submissions' : submissions,
                        'verdict' : submission_instance.verdict,
                        'submission_count' : Submission.objects.filter(problem_id = id).count(),
                        'accepted_count' : Submission.objects.filter(problem_id = id , verdict = getMessage(ACCEPTED)).count()
                        })
    
    print("user id : " , request.user.id)
    submissions = Submission.objects.filter(problem_id = id , user_id = request.user.id).order_by('submission_time').reverse()[:10] # add user id as well later on             
    problem = Problem.objects.filter(id = id).get()
    return render(request , "problem_details.html" ,
                  {'problem' : problem , 
                   'testcases' : problem.testcases.all(),
                   'submission_form' : SubmissionForm(),
                   'submissions' : submissions,
                   'submission_count' : Submission.objects.filter(problem_id = id).count(),
                   'accepted_count' : Submission.objects.filter(problem_id = id , verdict = getMessage(ACCEPTED)).count()
                   })

def standing(request) :
    users = CustomUser.objects.all()
    data = []
    for user in users :
        user_name = user
        user_id = user.id
        submission = Submission.objects.filter(user_id = user_id)
        submission_count = len(submission)
        problem_solved = Submission.objects.filter(user_id = user_id , verdict = getMessage(ACCEPTED)).values('problem_id').annotate(count = Count('problem_id')).count()
        data.append({
            "name" : user_name,
            "id" : user_id,
            "all" : submission_count,
            "ac" : problem_solved
        })
    
    data = sorted(data , key = lambda x : (-x['ac'] , -x['all']))
    return render(request , "standing_page.html" , {'data' : data})

def contribution(request) :
    users = CustomUser.objects.all()
    data = []
    for user in users :
        user_name = user
        user_id = user.id
        
        blogs = Blog.objects.filter(author = user_name)
        blog_count = blogs.count()
        
        contribution = 0
        
        for blog in blogs :
            contribution += Like.objects.filter(blog=blog).count()
            contribution -= Dislike.objects.filter(blog=blog).count()

        
        data.append({
            "name" : user_name,
            "id" : user_id,
            "contribution" : contribution,
            "blogs" : blog_count
        })
    
    data = sorted(data , key = lambda x : (-x['contribution'] , -x['blogs']))
    return render(request , "contribution_page.html" , {'data' : data})

def download_file(request , problem_id) :
    problem = Problem.objects.filter(id = problem_id).get()
    problem_name = problem.name
    problem_statement = problem.statement
    problem_input_desc = problem.input_description
    probelm_output_desc = problem.output_description
    problem_explanation = problem.explanation
    
    print(problem.__dict__)
    print("name : " , problem_name , problem_id)
    problem_testcase = []
    for testcase in problem.testcases.all() :
        print(testcase)
        if testcase.show :
            problem_testcase.append((testcase.input_text , testcase.output_text))
    
    create_problem_pdf(problem_name , problem_statement , problem_input_desc , probelm_output_desc , problem_testcase , problem_explanation)
    
    file_path = BASE_DIR + "problem_pdfs\\problem.pdf"
    try:
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="done.pdf"'
            return response
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)