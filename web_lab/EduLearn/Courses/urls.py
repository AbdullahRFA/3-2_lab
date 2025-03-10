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
    
]

