from django.shortcuts import render, redirect, get_object_or_404
from addBlog.models import Blog
from django.http import JsonResponse
from .models import Like, Dislike, Comment
from .forms import CommentForm
from django.urls import reverse
from django.utils import timezone

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


def blog_details(request , id , comment_id = None , error = "" , info = "") :
    blog = Blog.objects.filter(id = id).get()
    likes = Like.objects.filter(blog=blog).count()
    dislikes = Dislike.objects.filter(blog=blog).count()
    count = likes - dislikes
    
    def getTime(target_date) :
        current_date = timezone.now()
        days = (current_date - target_date).days
        seconds = (current_date - target_date).seconds
        minutes = seconds // 60
        hours = minutes // 60
        time = str(days) + " days ago"
        if days == 0 :
            time = str(hours) + " hours ago"
            if hours == 0 :
                time = str(minutes) + " minutes ago"
                if minutes == 0 : 
                    time = str(seconds) + " seconds ago"
        return time
        
    comments = Comment.objects.filter(blog=blog)
    comments_count = len(comments)
    mapping_to_comments = {}
    
    adj = {}
    
    for comment in comments.order_by('-created_at') :
        parent = comment.parent_comment
        mapping_to_comments[comment.id] = comment
        if parent == None :
            continue
        if parent.id not in adj.keys() :
            adj[parent.id] = []
        adj[parent.id].append(comment.id)
        
        
    hope_2 = []
    
    visited = {}
    
    def dfs(node , level) :
        visited[node] = True
        hope_2.append({
            "comment" : mapping_to_comments[node],
            "level" : [0 for _ in range(level)],
            "time" : getTime(mapping_to_comments[node].created_at)
        })
        if node not in adj.keys() :
            return
        for child in adj[node] :
            dfs(child , level + 1)
            
    for comment in comments.order_by('-created_at') :
        if comment.id not in visited.keys() and comment.parent_comment == None:
            dfs(comment.id , 0)
    
    recent_blogs = []
    
    for blog_ in Blog.objects.filter().order_by('-added_date') :
        recent_blogs.append({
            "id" : blog_.id,
            "author" : blog_.author,
            "title" : blog_.title,
            "time" : getTime(blog_.added_date)
        })
        
    print("like : " , likes)
    print("dislike : " , dislikes)
        
    return render(request , "blog_details_new.html", {'blog' : blog ,'likes' : likes, 'dislikes': dislikes,'count': count,'time':getTime(blog.added_date),'hope' : hope_2, 'comments_count' : comments_count , 'recent_blogs' : recent_blogs , 'comment_id_focus' : comment_id , 'error' : error , 'info' : info})

def blog_likes(request , id) :
    # storing like - dislike in likes only.
    user = request.user
    blog = Blog.objects.filter(id = id).get()
    
    current_likes = blog.likes
    liked = Like.objects.filter(user=user,blog=blog).count()
    disliked = Dislike.objects.filter(user = user , blog = blog).count()
    
    if disliked :
        return blog_details(request, id = id , error = "You already disliked the blog. First remove dislike to update.")
        
    print("like 0 : " , current_likes)
    
    if not liked:
        liked = Like.objects.create(user=user,blog=blog)
        current_likes = current_likes + 1
        info = "Like added"
    else:
        liked = Like.objects.filter(user=user,blog=blog).delete()
        current_likes = current_likes - 1
        info = "Like removed"
        
    blog.likes = current_likes
    print("like 1 : " , current_likes)
    blog.save()
    
    return blog_details(request , id=id , info = info)

def blog_dislikes(request , id) :
    user = request.user
    blog = Blog.objects.filter(id = id).get()
    
    current_dislikes = blog.dislikes
    disliked = Dislike.objects.filter(user=user,blog=blog).count()
    liked = Like.objects.filter(user=user,blog=blog).count()
    
    if liked :
        return blog_details(request , id = id , error = "You already liked the blog. First remove like to update.")
    
    if not disliked:
        disliked = Dislike.objects.create(user=user,blog=blog)
        current_dislikes = current_dislikes + 1
        info = "Dislike added"
    else:
        disliked = Dislike.objects.filter(user=user,blog=blog).delete()
        current_dislikes = current_dislikes - 1
        info = "Dislike removed"
        
    blog.dislikes = current_dislikes
    blog.save()
    
    return blog_details(request , id=id , info = info)




def add_comment(request, blog_id, comment_id = None):
    # Get the blog post
    blog = get_object_or_404(Blog, id=blog_id)

    # Initialize parent_comment as None
    parent_comment = None

    if comment_id:
        # If comment_id is provided, it's a reply to an existing comment
        parent_comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user  # Assuming user is logged in
            comment.parent_comment = parent_comment  # Set the parent comment
            comment.save()
            return redirect('blog_details', id=blog.id , comment_id = comment.id)

    # If the request method is not POST or the form is not valid, render the page
    form = CommentForm()

    # Fetch all top-level comments for the blog
    comments = Comment.objects.filter(blog=blog, parent_comment=None)

    return render(request, 'add_comment.html', {
        'blog': blog,
        'form': form
    })


def add_coomment_js(request , blog_id , comment_id) :
    data = {
        "value" : "done"
    }
    print("data : " , data)
    return JsonResponse(data)