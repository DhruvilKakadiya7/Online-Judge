from django import forms
from .models import Problem

class AddProblemForm(forms.ModelForm) :
    testcases = forms.JSONField()
    class Meta : 
        model = Problem
        exclude = ['added_date']
        labels = {
            'name': 'Name',
            'rating': 'Rating',
            'statement' : 'Problem Statement',
            'input_description' : 'Input Description',
            'output_description' : 'Output Description',
            'explanation' : 'Explanation'
        }