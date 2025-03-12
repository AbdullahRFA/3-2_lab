# from django.contrib import admin
from django.urls import path
from Courses import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.course_list,name='course_list'),
    path('<int:courseID>/', views.Course_details, name='coursedetails'),
    
    path('create_course/',views.create_course,name='create_course'),
    path('course_update/<int:id>/',views.course_update,name='course_update'),
    path('course_delete/<int:id>/',views.course_delete,name='course_delete'),
    
    path('lesson_create/',views.lesson_create,name='lesson_create'),
    path('lesson_update/<int:id>/',views.lesson_update,name='lesson_update'),
    path('lesson_delete/<int:id>/',views.lesson_delete,name='lesson_delete'),
    
    path('enroll_student/',views.enroll_student,name='enroll_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('student_update/<int:id>/',views.student_update,name='student_update'),
    path('student_delete/<int:id>/',views.student_delete,name='student_delete'),
    
    path('course_enrolled_student_all/',views.course_enrolled_student_all,name='course_enrolled_student_all'),
    path('course_enrolled_student/<int:id>',views.course_enrolled_student,name='course_enrolled_student'),
    path('individual_std_details/<int:id>',views.individual_std_details,name='individual_std_details'),
    path('individual_course_details/<int:id>',views.individual_course_details,name='individual_course_details'),
    
]

