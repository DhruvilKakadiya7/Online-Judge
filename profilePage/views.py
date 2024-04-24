from django.shortcuts import render, redirect
from django.http import HttpResponse
from register.models import CustomUser
from .forms import ProfileForm
from addBlog.models import Blog
from blogPage.models import Like, Dislike
from problemPage.models import Submission
from problemPage.config import *
from django.db.models import Count

# Create your views here.
def profile_page(request):
    blogs = Blog.objects.filter(author=request.user)
    blog_count = blogs.count()
    
    user_id = request.user.id
    problem_solved = Submission.objects.filter(user_id = user_id , verdict = getMessage(ACCEPTED)).values('problem_id').annotate(count = Count('problem_id')).count()
    
    likes = 0
    dislikes = 0

    for blog in blogs:
        likes += Like.objects.filter(blog=blog).count()
        dislikes += Dislike.objects.filter(blog=blog).count()

    contribution = likes - dislikes

    return render(request, "profile_page.html", {'blog_count': blog_count, 'contribution': contribution , 'problem_solved' : problem_solved})



def my_submissions(request , id) :
    print(request.user , request.user.id)
    submissions = Submission.objects.filter(user_id = request.user.id).order_by('submission_time').reverse()
    for each in submissions : 
        print(each)
    return render(request , "my_submissions.html" , {'submissions' : submissions})

def global_submissions(request) :
    submissions = Submission.objects.filter().order_by('submission_time').reverse()
    return render(request , "my_submissions.html" , {'submissions' : submissions})
    

def profile_setting(request):
    user = request.user
    form = ProfileForm(instance=user) 
    

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')

    return render(request, 'profile_setting.html', {'form': form})

    
       
 