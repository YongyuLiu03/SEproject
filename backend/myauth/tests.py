from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from courses.models import Student  # Assuming Student model exists
from .serializers import UserRegistrationSerializer

class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.student = Student.objects.create(user=self.user)
        self.token = Token.objects.create(user=self.user)

    def test_login_api_view_success(self):
        # Test login with correct credentials
        response = self.client.post('/api/login', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('coursesExist', response.data)

    def test_login_api_view_invalid_credentials(self):
        # Test login with incorrect credentials
        response = self.client.post('/api/login', {'username': 'testuser', 'password': 'wrongpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)

    def test_signup_api_view_success(self):
        # Test signup with valid data
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post('/api/signup', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # One existing user + newly created user

    def test_signup_api_view_invalid_data(self):
        # Test signup with invalid data
        data = {'username': '', 'password': 'newpassword'}  # Empty username
        response = self.client.post('/api/signup', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_api_view_success(self):
        # Test logout when authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/logout')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Token.objects.filter(user=self.user).exists())

    def test_logout_api_view_unauthenticated(self):
        # Test logout when not authenticated
        response = self.client.get('/api/logout')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Token.objects.filter(user=self.user).exists())
