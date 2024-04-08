from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Course, Major


class StudentSerializer(serializers.ModelSerializer):
    # major = serializers.SlugRelatedField(slug_field='name', queryset=Major.objects.all(), many=True)

    class Meta:
        model = Student
        fields = ['student_id', 'user', 'level_id', 'credit']
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        student = Student.objects.create(user=user, **validated_data)
        return student
    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'name', 'credit', 'description', 'at_fall', 'at_spring']

    def create(self, validated_data):
        course_id = validated_data.get('course_id')
        course, created = Course.objects.get_or_create(course_id=course_id, defaults=validated_data)
        if not created:
            for attr, value in validated_data.items():
                setattr(course, attr, value)
            course.save()
        return course
    