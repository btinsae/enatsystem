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
class Guardian(models.Model):
    first_name=models.CharField(max_length=100,blank=True)
    middle_name=models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100,blank=True)
    phone_no=models.CharField(max_length=100,blank=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,default='')
    def __str__(self):
         return self.first_name+' '+self.middle_name+' '+self.last_name

class StudentGroup(models.Model):
    group_name=models.CharField(max_length=100)
    def __str__(self):
        return self.group_name

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
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=30,null=True)
    gender=models.CharField(max_length=2,choices=GENDER,default=BLANK)
    nationality=models.CharField(max_length=15,default='Ethiopian')
    blood_group=models.CharField(max_length=2,choices=BLOOD_GROUP,default=UNKNOWN)
    joining_date=models.DateTimeField(default=timezone.now)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,default='')
    guardian=models.ForeignKey(Guardian,on_delete=models.CASCADE,default='')
    student_group=models.ForeignKey(StudentGroup,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name

class Teacher(models.Model):

    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=30,null=True)

    def __str__(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name



