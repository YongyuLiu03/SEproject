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
    """
    API endpoint for parsing and updating a student's course dictionary.

    Permission Classes:
        - IsAuthenticated: Only authenticated users can access this view.
    """
    
    permission_classes = [permissions.IsAuthenticated]
    cs = Major.objects.filter(name__iexact="cs").first()

    def get(self, request):
        """
        Retrieve the course dictionary for the authenticated student.

        Returns:
            Response: Response containing the serialized student data.
        """
        try:
            student = request.user.student
            course_dict = student.course_dict
            student_serializr = StudentSerializer(student)
            return Response({'student': student_serializr.data})
        except ObjectDoesNotExist:
            return Response("student does not exist, shouldn't get", 
                            status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        """
        Parse and update the course dictionary for the authenticated student.

        Args:
            request: The incoming HTTP request.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: Response containing the serialized student data.
        """
        update_course = request.data.get("updateCourse")
        course_dict = request.data.get('course_dict', '')
        parse_course = request.data.get('parseCourse', '')
        if parse_course: course_dict = parse_course_history(course_dict)
        else: course_dict = json.loads(course_dict)        
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
    """
    API endpoint for recommending courses based on a student's course dictionary.

    Permission Classes:
        - IsAuthenticated: Only authenticated users can access this view.
    """
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Retrieve recommended courses based on the authenticated student's course dictionary.

        Returns:
            Response: Response containing the recommended courses.
        """
        try:
            course_dict = request.user.student.course_dict
            identity = request.query_params.get('identity')
            intense = request.query_params.get('intense')
            if identity is not None and intense is not None:
                recommendor = Recommendor(course_dict, identity, intense)
                print(recommendor.recommend())
                valid, recommend_courses = recommendor.recommend()
                return Response({'valid': valid, 'recommend_courses': recommend_courses})
            else:
                return Response("Missing 'identity' or 'intense' parameter",
                                 status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response("student or course_dict does not exist",
                             status=status.HTTP_404_NOT_FOUND)


class CourseDetailAPIView(APIView):
    """
    API endpoint for retrieving details of a specific course.

    Permission Classes:
        - AllowAny: No permission required to access this view.
    """
    
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        """
        Retrieve details of a specific course.

        Args:
            request: The incoming HTTP request.
            id (int): The ID of the course to retrieve.

        Returns:
            Response: Response containing the course details.
        """
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
    """
    API endpoint for retrieving details of a specific major.

    Permission Classes:
        - AllowAny: No permission required to access this view.
    """
    
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, name):
        """
        Retrieve details of a specific major.

        Args:
            request: The incoming HTTP request.
            name (str): The name of the major to retrieve.

        Returns:
            Response: Response containing the major details.
        """
        try:
            major = Major.objects.filter(name__iexact=name).first()
            requirements = major.get_all_reqs()
            courses_list = [( req.count, "Elective" if req.elective else "Required", CourseSerializer(req.courses.all(), many=True).data) for req in requirements]
            return Response({"requirements": courses_list})
        except Major.DoesNotExist:
            return Response({"error": "Major not found"}, status=status.HTTP_404_NOT_FOUND)
        

class DisplayCoreAPIView(APIView):
    """
    API endpoint for displaying core courses based on location.

    Permission Classes:
        - AllowAny: No permission required to access this view.
    """
    
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        """
        Retrieve core courses based on location.

        Args:
            request: The incoming HTTP request.

        Returns:
            Response: Response containing the core courses.
        """
        loc = request.query_params.get('loc').lower()
        try:
            with open(f"courses/recommendor/{loc}_core_courses.json") as f:
                course_lists = json.load(f)
            return Response({'course_lists': course_lists})
        except FileNotFoundError:
            return Response({"error": "Location invalid"}, status=status.HTTP_404_NOT_FOUND)







