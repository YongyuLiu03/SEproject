from .models import Student
from .serializers import StudentSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView


class CourseScheduleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Link Student to the logged-in User
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Major, Timeslot
from .parse_course_history import parse_course_history

 


class CourseAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        
        # import pdb
        # pdb.set_trace()
        # if serializer.is_valid():
        #     html_content = serializer.validated_data['html_content']
        name, GPA, course_dict = parse_course_history(request.data['html'])
        hide_grade = request.data['hideGrade']
        print(hide_grade)
        return Response(course_dict)
        
