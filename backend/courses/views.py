from .models import Student, StudentTakenCourse, Major, Course
from .serializers import StudentSerializer, CourseSerializer, MajorSerializer, PrereqSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from .parse_course_history import parse_course_history
from .recommendor.recommendor import Recommendor

import json

class ParseCourseDictAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    cs = Major.objects.filter(name__iexact="cs").first()

    def get(self, request):
        try:
            student = request.user.student
            course_dict = student.course_dict
            student_serializr = StudentSerializer(student)
            return Response({'student': student_serializr.data})
        except ObjectDoesNotExist:
            return Response("student does not exist, shouldn't get", status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        update_course = request.data.get("updateCourse")
        course_dict = request.data.get('course_dict', '')
        parse_course = request.data.get('parseCourse', '')
        print(course_dict)
        print(parse_course)
        if parse_course: course_dict = parse_course_history(course_dict)
        student, created = Student.objects.get_or_create(user=request.user)
        if created:
            student.major.add(self.cs)
            student.course_dict = course_dict
            student.level_id = len(course_dict)
        if update_course:
            student.course_dict = course_dict
            student.level_id = len(course_dict)
        student.save()
        student_serializr = StudentSerializer(student)
        return Response({'student': student_serializr.data})


class RecommendCourseAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            course_dict = request.user.student.course_dict
            identity = request.query_params.get('identity')
            intense = request.query_params.get('intense')
            if identity is not None and intense is not None:
                recommendor = Recommendor(course_dict, identity, intense)
                valid, recommend_courses = recommendor.recommend()
                return Response({'valid': valid, 'recommend_courses': recommend_courses})
            else:
                return Response("Missing 'identity' or 'intense' parameter", status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            print("student or course_dict does not exist")
            return Response("student or course_dict does not exist", status=status.HTTP_404_NOT_FOUND)


class CourseDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        try:
            course = Course.objects.get(id=id)
            prereqs = course.get_prereqs()
            majors = course.get_fulfill_majors()
            course_serializer = CourseSerializer(course)
            prereq_serializer = PrereqSerializer(prereqs, many=True)
            major_serializer = MajorSerializer(majors, many=True)
            response_data = {
                'course': course_serializer.data,
                'prerequisites': prereq_serializer.data,
                'majors': major_serializer.data
            }
            return Response(response_data)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)


class MajorDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, name):
        try:
            print(name)
            major = Major.objects.filter(name__iexact=name).first()
            requirements = major.get_all_reqs()
            courses_list = [( req.count, "Elective" if req.elective else "Required", CourseSerializer(req.courses.all(), many=True).data) for req in requirements]
            return Response({"requirements": courses_list})
        except Major.DoesNotExist:
            return Response({"error": "Major not found"}, status=status.HTTP_404_NOT_FOUND)
        

class DisplayCoreAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        loc = request.query_params.get('loc').lower()
        try:
            with open(f"courses/recommendor/{loc}_core_courses.json") as f:
                course_lists = json.load(f)
            return Response({'course_lists': course_lists})
        except FileNotFoundError:
            return Response({"error": "Location invalid"}, status=status.HTTP_404_NOT_FOUND)







