# from django.contrib import admin
from django.urls import path
from Courses import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('description/',views.descriptions,name='description'),
    
]