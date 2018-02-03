from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students',views.students,name='students'),
    path('student/<int:student_id>',views.student)
]