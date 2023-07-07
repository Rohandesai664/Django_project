from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from student.models import Student , Teacher ,Class
from student.serializers import StudentSerializers , TeacherSerializers , ClassSerializers
import json


# Create your views here.
@csrf_exempt
def StudentApi(request ,studentid=0):
   
    if request.method == 'GET':
        value = request.GET.get('name')
        print(value)
        if studentid ==0 :
            student_info = Student.objects.all()
            student_ser = StudentSerializers(student_info , many = True)
            return JsonResponse(student_ser.data,safe=False)
        else:
            student = Student.objects.get(StudentId = studentid)
            student_ser = StudentSerializers(student)
            return JsonResponse(student_ser.data , safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        print( type (student_data))
        student_ser = StudentSerializers(data=student_data)
        if student_ser.is_valid():
            student_ser.save()
            return JsonResponse("added successfully",safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Student.objects.get(StudentId = student_data["StudentId"])
        student_ser = StudentSerializers(student,data=student_data)
        if student_ser.is_valid():
            student_ser.save()
            return JsonResponse("update successfully", safe=False)
        return JsonResponse("failed ")
    elif request.method == 'DELETE':
        try:
            student = Student.objects.get(StudentId = studentid)
        except Student.DoesNotExist:
            return JsonResponse("data doest not exit", safe=False)
        else:
            student.delete()
            return JsonResponse("deleted successfully", safe= False)
    


@csrf_exempt
def TeacherApi(request , teacherid = 0):
    if request.method == 'GET':
        teacher_data = Teacher.objects.all()
        print(teacher_data)
        teacher_ser = TeacherSerializers(teacher_data,many=True)
        return JsonResponse(teacher_ser.data,safe=False)
    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        try:
            teacher = Teacher.objects.get(TeacherId=teacher_data["TeacherId"])
        except Teacher.DoesNotExist:
            return JsonResponse("Student not found", safe=False)
        else:
            teacher_ser = TeacherSerializers(teacher)
            return JsonResponse(teacher_ser.data, safe=False)
        
    elif request.method == 'PUT':
        teacher_data = JSONParser().parse(request)
        teacher = Teacher.objects.get(TeacherId = teacher_data["TeacherId"])
        print(teacher)
        teacher_ser = TeacherSerializers(teacher , data=teacher_data)
        if teacher_ser.is_valid():
            teacher_ser.save()
            return JsonResponse("update succesfully", safe=False)
        return JsonResponse('failed to update',safe=False)
    elif request.method == 'DELETE':
        try:
            teacher= Teacher.objects.get(TeacherId = teacherid)
        except Student.DoesNotExist:
            return JsonResponse("data doest not exit", safe=False)
        else:
            teacher.delete()
            return JsonResponse("deleted successfully", safe= False)
    
@csrf_exempt
def ClassApi(request , classid = 0):
    if request.method == 'GET':
        class_data = Class.objects.all()
        class_ser = ClassSerializers(class_data,many=True)
        return JsonResponse(class_ser.data,safe=False)
    elif request.method == 'POST':
        class_data = JSONParser().parse(request)
        class_ser = ClassSerializers(data=class_data)
        if class_ser.is_valid():
            class_ser.save()
            return JsonResponse('added successfully',safe=False)
        return JsonResponse('failed' , safe=False)
    elif request.method == 'PUT':
        class_data = JSONParser().parse(request)
        class_info = Teacher.objects.get(TeacherId = class_data["TeacherId"])
        class_ser = ClassSerializers(class_info , data=class_data)
        if class_ser.is_valid():
            class_ser.save()
            return JsonResponse("update succesfully",safe=False)
        return JsonResponse('failed to update',safe=False)
    elif request.method == 'DELETE':
        try:
            class_data = Class.objects.get(ClassId = classid)
        except Student.DoesNotExist:
            return JsonResponse("data doest not exit", safe=False)
        else:
            class_data.delete()
            return JsonResponse("deleted successfully", safe= False)