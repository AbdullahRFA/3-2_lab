from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    thumbnail = models.ImageField(upload_to='course_thumbnail/',null=True,blank=True)
    
    def __str__(self):
        return self.title + ' ( ' + str(self.duration)+ ' ) '
    
    
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='lessons')
    
    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField(Courses, related_name='students')
    
    def __str__(self):
        return self.name