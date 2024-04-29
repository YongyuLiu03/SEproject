from .models import Student, StudentTakenCourse, Major, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from .parse_course_history import parse_course_history
# from recommendor.recommendor import filter_core_courses, filter_elective_courses, filter_major_courses



class ParseCourseDictAPIView(APIView):
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
        update_course = request.data.get("updateCourse")
        course_dict = parse_course_history(request.data['html'])
        cs = Major.objects.get(name="cs")
        if update_course:          
            student = Student.objects.get(user=request.user)
            student.course_dict = course_dict
            student.level_id = len(course_dict)
            student.save()
        else:
            student, created = Student.objects.create(
                user=request.user, course_dict=course_dict, level_id=len(course_dict), major=cs)
        
        student.add_taken_courses()
        student.calc_taken_credit()

        return Response(course_dict)

# class 

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

