# from django.contrib import admin
from django.urls import path
from Courses import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('<int:courseID>/', views.Course_details, name='coursedetails'),
    path('description/',views.descriptions,name='description'),
    path('course_update/<int:id>/',views.course_update,name='course_update'),
    path('course_delete/<int:id>/',views.course_delete,name='course_delete'),
    path('lesson_create/',views.lesson_create,name='lesson_create'),
    
]

