# courses/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    path('api/taken-courses', views.ParseCourseDictAPIView.as_view(), name='taken-courses-api'),
    path('api/core-courses', views.DisplayCoreAPIView.as_view(), name="core-courses-api"),
    path('api/courses/<str:id>', views.CourseDetailAPIView.as_view(), name='course-detail'),
    path('api/majors/<str:name>', views.MajorDetailAPIView.as_view(), name='major-detail'),
    path('api/rec-courses', views.RecommendCourseAPIView.as_view(), name='rec-courses'),
]
