from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('This is HOME page')
    return render(request,'Courses/index.html')
def descriptions(request):
    return render(request,'Courses/description.html')