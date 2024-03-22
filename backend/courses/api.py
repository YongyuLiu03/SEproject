from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, TakenCourse, CurrentSemesterCourse, UserCourse
from .serializers import HTMLSerializer
from .parse_course_history import parse_course_history




class CourseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = HTMLSerializer(data=request.data)
        # import pdb
        # pdb.set_trace()
        # if serializer.is_valid():
        #     html_content = serializer.validated_data['html_content']
        name, GPA, course_dict = parse_course_history(request.data['html'])
        return Response(course_dict)

        # # Placeholder
        #     parsed_data = {
        #         "2024 Spring": [["Math 101", "A"], ["History 101", "B"]],
        #         "2023 Fall": [["Science 101", "A-"], ["English 101", "B+"]]
        #     }

        #     return Response({"message": "HTML processed"})
    
        return Response(serializer.errors, status=400)
    
        # for semester, courses in parsed_data.items():
        #     for course_name, grade in courses:
        #         course, created = TakenCourse.objects.get_or_create(
        #             name=course_name, semester=semester)
                
        #         UserCourse.objects.create(
        #             user=request.user,
        #             course=course,
        #             grade=grade
        #         )
                
        # # return Response({"status": "courses saved successfully"})
    
    
