from django.shortcuts import render, redirect, get_object_or_404
from addBlog.models import Blog
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


def blog_details(request , id) :
    blog = Blog.objects.filter(id = id).get()
    likes = Like.objects.filter(blog=blog).count()
    dislikes = Dislike.objects.filter(blog=blog).count()
    count = likes-dislikes
    current_date = timezone.now()
    days = (current_date - blog.added_date).days
    comments = Comment.objects.filter(blog=blog)
    
    
    # Assuming you've already fetched your comments
    # comment_dict = {}

    # for comment in comments:
    #     # print(comment.parent_comment)
    #     if comment.parent_comment is None:
    #         # This is a top-level comment
    #         comment_dict[comment] = []
            
            
    # hope = []
    
    # for comment in comments :
    #     level = []
    #     print(comment.text)
    #     origin_comment = comment
    #     while comment.parent_comment != None :
    #         level.append("hope")
    #         comment = comment.parent_comment
    #         if comment == None : break
    #         print(" " * len(level) + comment.text)
    #     hope.append({
    #         "comment" : origin_comment,
    #         "level" : level
    #     })
    
    
    mapping_to_comments = {}
    
    adj = {}
    
    for comment in comments :
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
            "level" : [0 for _ in range(level)]})
        if node not in adj.keys() :
            return
        for child in adj[node] :
            dfs(child , level + 1)
            
    for comment in comments :
        if comment.id not in visited.keys() :
            dfs(comment.id , 0)
    
    

    # for comment in comments:
    #     print(comment)
    #     if comment.parent_comment is not None and comment.parent_comment in comment_dict:
    #         # This comment is a reply to an existing comment
    #         comment_dict[comment.parent_comment].append(comment)
    # print(comment_dict)
# Pass comment_dict to the template

    return render(request , "blog_details.html", {'blog' : blog ,'likes' : likes, 'dislikes': dislikes,'count': count,'days':days,'hope' : hope_2})

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
            return redirect('blog_details', id=blog.id)

    # If the request method is not POST or the form is not valid, render the page
    form = CommentForm()

    # Fetch all top-level comments for the blog
    comments = Comment.objects.filter(blog=blog, parent_comment=None)

    return render(request, 'add_comment.html', {
        'blog': blog,
        'form': form
    })


