from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Course, Major, CoursePrereq


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'

class PrereqSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePrereq
        fields = '__all__'
