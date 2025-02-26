from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404
from .models import Lesson,Courses,Student
# Create your views here.
def home(request):
    courses = Courses.objects.all()
    return render(request,'Courses/index.html',{'courses':courses})


def descriptions(request):
    courses = Courses.objects.all()
    return render(request,'Courses/description.html',{'courses':courses})

def Course_details(request, courseID):
    courses = get_object_or_404(Courses, id=courseID)
    lessons = courses.lessons.all()  # Correct way to access related lessons
    return render(request, 'Courses/description.html', {'lessons': lessons, 'courses': courses})