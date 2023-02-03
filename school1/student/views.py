from django.shortcuts import render
#from .models import student 
# Create your views here.
def abu(request):
    return render(request, 'students/abu.html')
     #{'students':student.objects.all()}
