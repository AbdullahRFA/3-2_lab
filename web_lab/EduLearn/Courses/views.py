from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from .models import Lesson,Courses,Student
from django.contrib.auth.decorators import login_required
from .forms import courseForm, LessonForm, StudentForm
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

def enroll_student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Student Enrolled Successfully!")

            # Get the first course the student enrolled in
            course = student.enrolled_courses.first()
            context = {
                'student': student,
                'course': course
            }

            return render(request, "Courses/enrollment_success_page.html", context)
    
    return render(request, "Courses/enrollment_form.html", {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request,'Courses/student_list.html',{"students":students})

def student_update(request,id):
    student = get_object_or_404(Student,id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Student update successful")
            return redirect('student_list')
    return render(request,"Courses/enrollment_form.html", {'form': form,'check':1})

def student_delete(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.delete()
        messages.warning(request,"Student deleted sucessfully")
        return redirect('student_list')
    return render(request,"Courses/student_confirm_delete.html",{'student':student})

def course_enrolled_student(request):
    courses = Courses.objects.prefetch_related('students').all()  # Fetch courses with enrolled students
    return render(request, "Courses/course_enrolled_student.html", {'courses': courses})


def individual_std_details(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "Courses/individual_std_details.html", {'student': student})

def individual_course_details(request, id):
    course = get_object_or_404(Courses, id=id)
    return render(request, "Courses/individual_course_details.html", {'course': course})