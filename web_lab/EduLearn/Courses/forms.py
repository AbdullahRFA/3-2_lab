from django import forms
from .models import Courses,Lesson

class courseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = 'All'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'duration':forms.NumberInput(attrs={'class':'form-control'})
        
        }
        
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
        widgets = {
        'course': forms.Select(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control'}),
        }