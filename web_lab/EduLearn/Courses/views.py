from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from .models import Lesson,Courses,Student
from django.contrib.auth.decorators import login_required
from .forms import courseForm, LessonForm
from django.contrib import messages

# Create your views here.
def course_list(request):
    courses = Courses.objects.all()
    return render(request,'Courses/index.html',{'courses':courses})


def Course_details(request, courseID):
    courses = get_object_or_404(Courses, id=courseID)
    lessons = courses.lessons.all()  # Correct way to access related lessons
    return render(request, 'Courses/course_details.html', {'lessons': lessons, 'courses': courses})

def create_course(request):
    form = courseForm()
    if request.method == "POST":
        form = courseForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Course created successfully!")
        return redirect('course_list')
    else:
        form = courseForm()
    return render(request, 'courses/course_form.html', {'form': form})
    
def course_update(request,id):
    form = courseForm()
    course = get_object_or_404(Courses, id=id)
    if request.method == "POST":
        form = courseForm(request.POST, request.FILES, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "Course updated successfully!")
        return redirect('course_list')
    else:
        form = courseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})
    
def course_delete(request,id):
    course = get_object_or_404(Courses, id=id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect('course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})
    


def lesson_create(request):
    form = LessonForm()
    if request.method == "POST":
        form = LessonForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Lesson created successfully!")
        return redirect('course_list')
    else:
        form = LessonForm()
    return render(request, 'Courses/lesson_form.html', {'form': form})
def lesson_update(request,id):
    lesson = get_object_or_404(Lesson,id=id)
    form = LessonForm()
    if request.method == "POST":
        form = LessonForm(request.POST,request.FILES,instance=lesson)
    if form.is_valid():
        form.save()
        messages.success(request,"Lesson Update successfully!")
        redirect('course_list')
    else:
        form = LessonForm(instance=lesson)
    return render(request,'Courses/lesson_form.html',{'form':form})

def lesson_delete(request,id):
    lesson = get_object_or_404(Lesson,id=id)
    if request.method == "POST":
        lesson.delete()
        messages.warning(request,"Lesson successfully deleted")
        return redirect('course_list')
    return render(request,'Courses/lesson_confirm_delete.html')