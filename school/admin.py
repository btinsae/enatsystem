from django.contrib import admin
from .models import Student,Teacher,StudentGroup,Guardian,Address,Course
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentGroup)
admin.site.register(Guardian)
admin.site.register(Address)
admin.site.register(Course)

