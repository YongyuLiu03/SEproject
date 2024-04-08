from .models import Student, Student_taken_Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from .parse_course_history import parse_course_history


class CourseAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        
        test_student_data = {"level_id": 4, "major": ["CS"], "credit": 120}

        try:
            student = request.user.student
            print("student exist")
        except ObjectDoesNotExist:
            student_serializer = StudentSerializer(data=test_student_data, context={'request': request})
            if student_serializer.is_valid():
                print("saving new student")
                student = student_serializer.save()
            else:
                print("student save failed")
                print(student_serializer.errors)
                return Response(student_serializer.errors, status=400)

        name, GPA, course_dict = parse_course_history(request.data['html'])

        for semester in course_dict:
            for course_list in course_dict[semester]:
                course_data = {
                    'course_id': course_list[0],
                    'name': course_list[1],
                    'credit': int(course_list[2])
                }
                serializer = CourseSerializer(data=course_data)
                if serializer.is_valid():
                    print("saving courses")
                    course = serializer.save()
                    student_course_data = {
                        'student_id': student,
                        'course_id': course,
                        'semester': semester
                    }
                    Student_taken_Course.objects.create(**student_course_data)

                else:
                    print(serializer.errors)

        return Response(course_dict)
        



