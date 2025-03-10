from django.contrib import admin
from .models import Courses, Lesson, Student

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'duration', 'thumbnail']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'course']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'get_enrolled_courses']

    def get_enrolled_courses(self, obj):
        return ", ".join([course.title for course in obj.enrolled_courses.all()])  # Display course titles
    get_enrolled_courses.short_description = 'Enrolled Courses'  # Column header

admin.site.register(Courses, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)