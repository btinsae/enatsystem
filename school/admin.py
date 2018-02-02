from django.contrib import admin
from .models import Student,Teacher,StudentGroup,Guardian,Address,Course,Assesment,StudentAssesment,Attendance
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentGroup)
admin.site.register(Guardian)
admin.site.register(Address)
admin.site.register(Course)
admin.site.register(Assesment)
admin.site.register(StudentAssesment)
admin.site.register(Attendance)

