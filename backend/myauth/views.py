from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class LoginAPIView(APIView):
    """
    API endpoint for user login.

    This endpoint allows users to authenticate and obtain an authentication token.

    Permission Classes:
        - AllowAny: No permission required to access this view.
    """

    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        """
        Authenticate user and generate authentication token.

        Args:
            request: The incoming HTTP request.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: Response containing the authentication token.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            has_student = hasattr(user, 'student')
            return Response({'token': token.key, "coursesExist": has_student})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class SignupAPIView(APIView):
    """
    API endpoint for user registration.

    This endpoint allows users to register and create a new account.

    Permission Classes:
        - AllowAny: No permission required to access this view.
    """
    
    permission_classes = [AllowAny]  
    def post(self, request):
        """
        Register a new user.

        Args:
            request: The incoming HTTP request.

        Returns:
            Response: Response indicating success or failure of user registration.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    """
    API endpoint for user logout.

    This endpoint allows authenticated users to logout and invalidate their authentication token.

    Authentication Classes:
        - TokenAuthentication: Token-based authentication required to access this view.
    
    Permission Classes:
        - IsAuthenticated: Only authenticated users can access this view.
    """


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Logout the user and invalidate the authentication token.

        Args:
            request: The incoming HTTP request.

        Returns:
            Response: Response indicating success of user logout.
        """
        request.user.auth_token.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

