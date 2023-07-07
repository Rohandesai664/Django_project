from django.db import models

# Create your models here.
class StudentInformation(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    StudentLoc = models.CharField(max_length=100)
    Standard = models.CharField(max_length=100)
    StudentAge = models.IntegerField()

   


class Teacher(models.Model):
    TeacherId = models.AutoField(primary_key=True)
    TeacherName = models.CharField(max_length=100)
    TeacherLoc = models.CharField(max_length=100)
    Division = models.CharField(max_length=100)
    TeacherAge = models.IntegerField()
    StudentDeatils = models.ForeignKey(Student,on_delete=models.CASCADE,default=None)

    

class Class(models.Model):
    ClassId = models.AutoField(primary_key=True)
    TeacherName = models.CharField(max_length=100)
    