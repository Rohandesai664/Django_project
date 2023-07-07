from rest_framework import serializers
from student.models import Student , Teacher , Class

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('StudentId','StudentName','StudentLoc','Standard','StudentAge')

    def validate_StudentAge(self,value):
        if value < 5 or value > 24:
            raise serializers.ValidationError("invalid age")
        return value
    

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('TeacherId','TeacherName','TeacherLoc','Division','TeacherAge')




class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('ClassId','TeacherName' )

