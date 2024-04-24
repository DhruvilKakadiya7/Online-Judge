from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from addProblem.models import Problem
from problemPage.models import Submission
from problemPage.config import *
from addBlog.models import Blog
from blogPage.models import Comment , Like , Dislike
from register.models import CustomUser
from django.db.models import Count

# Create your views here.
def dashboard(request) :
    recent_problem = Problem.objects.all().order_by('-added_date').first()
    submissions = Submission.objects.filter(problem_id = recent_problem.id).count()
    solved = Submission.objects.filter(problem_id = recent_problem.id , verdict = getMessage(ACCEPTED)).count()
    
    recent_blog = Blog.objects.all().order_by('-added_date').first()
    
    votes = recent_blog.likes - recent_blog.dislikes
    comment_count = Comment.objects.filter(blog = recent_blog).count()
    if submissions == 0 :
        accuracy = 0
    else :
        accuracy = round(solved * 100 / submissions , 2)
        
        
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
    
    ranks = []
    count = 5
    rank = 1
    
    for each in data :
        if count == 0 :
            break
        count -= 1
        
        ranks.append({
            "rank" : rank,
            "name" : each['name'],
            "ac" : each['ac']
        })
        
        rank += 1
        
        
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
    
    contributions = []
    
    rank = 1
    count = 5
    
    for each in data :
        if count == 0 :
            break
        count -= 1
        
        contributions.append({
            "rank" : rank,
            "name" : each['name'],
            "contribution" : each['contribution']
        })
    
        
    return render(request , "dashboard.html" , {'problem' : recent_problem , 'submissions' : submissions , 'ac' : solved , 'accuracy' : accuracy , 'blog' : recent_blog , 'vote' : votes , 'comment_count' : comment_count , 'ranks' : ranks , 'contributions' : contributions})

def hope(request) :
    data = {
        "value" : "We are done now. Time : " + str(datetime.now().second)
    }
    return JsonResponse(data)