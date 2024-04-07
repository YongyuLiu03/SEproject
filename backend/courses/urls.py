# courses/urls.py

from django.urls import path
from .views import CourseAPIView

urlpatterns = [
    path('api/courses/', CourseAPIView.as_view(), name='courses-api'),
]
