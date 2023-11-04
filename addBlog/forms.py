from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm) :
    
    class Meta : 
        model = Blog
        exclude = ['added_date','author','likes','dislikes']
        
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image' : 'Add Image',
        }