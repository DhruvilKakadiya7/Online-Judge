from django.shortcuts import render
from .forms import AddBlogForm
from datetime import datetime
from .models import Blog

# Create your views here.

def add_blog_page(request) :
    
    if request.method == "POST" :

        title = request.POST['title']
        content = request.POST['content']
        image = request.POST['image']
        time = datetime.now()
        
        model = Blog(
            title = title,
            content = content,
            image = image,
            author=request.user,
        )
        
        model.save()
        
    return render(request,"add_blog_page.html",{'form': AddBlogForm()})
    
