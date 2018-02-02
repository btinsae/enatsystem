from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(request):
    return render(request,'school/index.html')

def students(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'school/student.html',{'context':context})

