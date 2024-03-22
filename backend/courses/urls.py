# courses/urls.py

from django.urls import path
from .api import CourseAPIView

urlpatterns = [
    path('api/courses/', CourseAPIView.as_view(), name='courses-api'),
]
