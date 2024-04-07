from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'level_id', 'major', 'credit']
        read_only_fields = ('student_id',)

    def create(self, validated_data):
        # `user` is not in `validated_data` so it must be added from the `save` method
        return Student.objects.create(**validated_data)
    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'name', 'credit', 'description', 'at_fall', 'at_spring']
        fields = '__all__'  # Include all fields from the model in the serializer
