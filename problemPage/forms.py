from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm) :
    class Meta : 
        model = Submission
        fields = [
            'problem_id',
            'user_id',
            'language',
            'source_file'
        ]