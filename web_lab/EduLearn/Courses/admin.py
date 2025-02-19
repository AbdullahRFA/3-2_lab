from django.contrib import admin
from .models import Courses, Lesson, Student
# Register your models here.
admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(Student)
