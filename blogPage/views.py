from django.shortcuts import render, redirect
from addBlog.models import Blog
from .models import Like, Dislike
from django.urls import reverse
# Create your views here.
def blog_page(request) :
    
    if request.method == "POST" :
        voteFilter = request.POST['filter1']
        dateFilter = request.POST['filter2']
        
        if voteFilter=="lth":
            blog = Blog.objects.filter().order_by('likes')
        else:
            blog = Blog.objects.filter().order_by('-likes')
            
        if dateFilter=="otn":
            blog = Blog.objects.filter().order_by('added_date')
        else:
            blog = Blog.objects.filter().order_by('-added_date')
            
        
        
        
        return render(request , "blog_page.html" , {'blog' : blog})
    
    blog = Blog.objects.filter().order_by('-added_date')
   
    return render(request , "blog_page.html" , {'blog' : blog}) 


def blog_details(request , id) :
    blog = Blog.objects.filter(id = id).get()
    likes = Like.objects.filter(blog=blog).count()
    dislikes = Dislike.objects.filter(blog=blog).count()
    return render(request , "blog_details.html", {'blog' : blog ,'likes' : likes, 'dislikes': dislikes})


def blog_likes(request , id) :
    user = request.user
    blog = Blog.objects.filter(id = id).get()
    
    current_likes = blog.likes
    liked = Like.objects.filter(user=user,blog=blog).count()
    
    if not liked:
        liked = Like.objects.create(user=user,blog=blog)
        current_likes = current_likes + 1
    else:
        liked = Like.objects.filter(user=user,blog=blog).delete()
        current_likes = current_likes - 1
        
    blog.likes = current_likes
    blog.save()
    
    return redirect('blog_details', id=id)

def blog_dislikes(request , id) :
    user = request.user
    blog = Blog.objects.filter(id = id).get()
    
    current_dislikes = blog.dislikes
    disliked = Dislike.objects.filter(user=user,blog=blog).count()
    
    if not disliked:
        disliked = Dislike.objects.create(user=user,blog=blog)
        current_dislikes = current_dislikes + 1
    else:
        disliked = Dislike.objects.filter(user=user,blog=blog).delete()
        current_dislikes = current_dislikes - 1
        
    blog.dislikes = current_dislikes
    blog.save()
    
    return redirect('blog_details', id=id)