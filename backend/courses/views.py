from .models import Student, Student_taken_Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from .parse_course_history import parse_course_history
from .course_recommend import filter_core_courses, filter_elective_courses, filter_major_courses



class CourseAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            student = request.user.student
            course_dict = student.course_dict
            print("student and course_dict exist")
            return Response(course_dict)
        except ObjectDoesNotExist:
            print("student or course_dict does not exist, shouldn't get")
            return Response("student or course_dict does not exist, shouldn't get", status=400)


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
            
        course_dict = parse_course_history(request.data['html'])
        student.course_dict.save_or_update(course_dict)
        student.save()

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
        

ny_electives = {}
sh_electives = {}


class TempInfoAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        student = request.student.user
        # untaken_major_courses = filter_major_courses(student.course_dict)
        # elective_courses = filter_elective_courses(student.course_dict, ny_electives, sh_electives)
        # taken_electives = filter_elective_courses(course_history, ny_elective_courses, sh_elective_courses)

        elective_courses = ['ED', 'HPC']
        untaken_major_courses = [['CSCI-SHU 220 Algorithms', 'CS-UY 2413 Design & Analysis of Algorithms', 'CSCI-GA 1170 Fundamental Algorithms', 'CSCI-UA 310 Basic Algorithms'],
        ['CSCI-SHU 420 Computer Science Senior Project']]
        taken_electives = ['CSCI-SHU 360', 'DATS-SHU 240']

        return Response(elective_courses, untaken_major_courses, taken_electives)


class DisplayCoreAPIView(APIView):
    
    core_courses = {}
    def get(self, request):
        Response(self.core_courses)
