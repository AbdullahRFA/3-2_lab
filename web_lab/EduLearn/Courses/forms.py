from django import forms
from .models import Courses,Lesson, Student

class courseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title','description','duration','thumbnail']
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
        
        
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'enrolled_courses']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # ✅ Fixed typo
            'enrolled_courses': forms.CheckboxSelectMultiple(),  # ✅ Fixed ManyToManyField issue
        }