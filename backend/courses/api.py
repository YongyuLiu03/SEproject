from rest_framework.views import APIView
from rest_framework.response import Response

class CourseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Placeholder for parsing logic
        parsed_data = {
            "2024 Spring": [["Math 101", "A"], ["History 101", "B"]],
            "2023 Fall": [["Science 101", "A-"], ["English 101", "B+"]]
        }
        return Response(parsed_data)