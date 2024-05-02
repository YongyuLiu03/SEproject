from django.urls import path
from .views import LoginAPIView, SignupAPIView, LogoutAPIView


urlpatterns = [
    path('api/login', LoginAPIView.as_view(), name='api-login'),
    path('api/signup', SignupAPIView.as_view(), name='api-signup'),
    path('api/logout', LogoutAPIView.as_view(), name='api-logout'),
]
