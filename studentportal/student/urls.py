from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('student',views.StudentApi),
    path('student/<int:studentid>',views.StudentApi),
    path('student/',views.StudentApi),
    path('teacher', views.TeacherApi),
    path('teacher/<int:teacherid>',views.TeacherApi),
    path('class',views.ClassApi),
    path('class/<int:classid>', views.ClassApi)
    
   
    
]
