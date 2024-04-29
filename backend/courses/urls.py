# courses/urls.py

from django.urls import path
from .views import CourseAPIView, DisplayCoreAPIView, TempInfoAPIView

urlpatterns = [
    path('api/courses/', CourseAPIView.as_view(), name='courses-api'),
    path('api/core-courses', DisplayCoreAPIView.as_view(), name="core-courses-api"),
    path('api/temp-info', TempInfoAPIView.as_view(), name='temp-info-api')
]
