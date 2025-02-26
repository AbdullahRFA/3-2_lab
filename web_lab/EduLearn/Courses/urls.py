# from django.contrib import admin
from django.urls import path
from Courses import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('<int:courseID>/', views.Course_details, name='coursedetails'),
    path('description/',views.descriptions,name='description'),
    
]

