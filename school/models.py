from django.db import models
from django.utils import timezone
# Create your models here.
class Address(models.Model):

    address_one=models.CharField(max_length=100)
    address_two=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    def __str__(self):
       return self.city+','+self.state+','+self.address_one
class Course(models.Model):
    course_name=models.CharField(max_length=100)

class Guardian(models.Model):
    full_name=models.CharField(max_length=20)  
    phone_no=models.CharField(max_length=100,blank=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,default='')
    def __str__(self):
         return self.full_name

class StudentGroup(models.Model):
    group_name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.group_name
class Assesment(models.Model):
    """Assesment class"""
    assesment_type=models.CharField(max_length=50)
    assesment_amount=models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.assesment_type

class Student(models.Model):
    MALE='M'
    FEMALE='F'
    BLANK=''

    GENDER = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'), 
        (BLANK, '')        
    )

    A= 'A'
    B= 'B'
    O= 'O'
    AB= 'AB'
    APLUS= 'A+'
    BPLUS= 'B+'
    UNKNOWN= ''

    BLOOD_GROUP= (        
        (A, 'A'),
        (B, 'B'),
        (O, 'O'),
        (AB, 'AB'),
        (APLUS, 'A+'),
        (BPLUS, 'B+'),
        (UNKNOWN, '')
    )
    full_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=30,null=True)
    gender=models.CharField(max_length=2,choices=GENDER,default=BLANK)
    nationality=models.CharField(max_length=15,default='Ethiopian')
    blood_group=models.CharField(max_length=2,choices=BLOOD_GROUP,default=UNKNOWN)
    joining_date=models.DateTimeField(default=timezone.now)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,default='')
    guardian=models.ForeignKey(Guardian,on_delete=models.CASCADE,default='')
    student_group=models.ForeignKey(StudentGroup,on_delete=models.CASCADE,default='')
    assesments=models.ManyToManyField(Assesment,through='StudentAssesment')
    def __str__(self):
        return self.full_name

class Teacher(models.Model):

    
    full_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=30,null=True)

    def __str__(self):
        return self.full_name



    #course=models.ForeignKey(Course,on_delete=models.CASCADE,default='')
class StudentAssesment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    assesment=models.ForeignKey(Assesment,on_delete=models.CASCADE)
    assesment_date=models.DateTimeField(auto_now_add=True)
    result=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.student.full_name +" "+self.assesment.assesment_type

class Attendance(models.Model):
    attend=models.BooleanField(default=False)
    date=models.DateField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.full_name + ' '+str(self.date)
class Fee(models.Model):
    for_month=models.DateField()
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=5, decimal_places=2)
    paid_on=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return self.student.full_name+' '+str(self.for_month)