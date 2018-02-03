from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.


def index(request):
    return render(request, 'school/index.html')


def students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'school/student.html', {'context': context})


def student(request, student_id=1):
    #try:
    student = Student.objects.get(pk=student_id)
    #except Entry.DoesNotExist:
     # print('Student not found')
    context = {'student': student}
    return render(request, 'school/student_detail.html', {'context': context})
