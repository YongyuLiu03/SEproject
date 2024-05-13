from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from courses.models import Course, Student, StudentTakenCourse
from django.urls import reverse
from unittest.mock import patch
from courses.serializers import StudentSerializer

class CourseAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.url = reverse('taken-courses-api')

        self.mock_html = "<html>Mock HTML content</html>"
        self.mock_course_dict = {
            'Fall 2021': [
                ['CSCI-SHU 101', 'Intro to Computer Science', '4']
            ],
            'Spring 2023': [
                ['MATH-SHU 101', 'Calculus I', '4']
            ]
        }
         
    # def test_successful_student_and_course_creation(self):
    #     with patch('courses.views.parse_course_history', return_value=(None, None, self.mock_course_dict)):
    #         response = self.client.post(self.url, {'html': self.mock_html}, format='json')
            
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertTrue(Student.objects.exists())
    #         self.assertTrue(Course.objects.exists())
    #         self.assertTrue(StudentTakenCourse.objects.exists())

    def test_student_serializer_with_invalid_data(self):
        invalid_student_data = {"level_id": 5, "major": ["Invalid"], "credit": 120}
        serializer = StudentSerializer(data=invalid_student_data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('major', serializer.errors)


    def test_unauthorized_access(self):
        self.client.logout() 
        
        response = self.client.post(self.url, {'html': self.mock_html}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


