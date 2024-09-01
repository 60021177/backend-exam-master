from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1 import school, classroom, teacher, student

router = DefaultRouter()

router.register('schools', school.SchoolViewSet, basename='school')
router.register('classrooms', classroom.ClassroomViewSet, basename='classroom')
router.register('teachers', teacher.TeacherViewSet, basename='teacher')
router.register('students', student.StudentViewSet, basename='student')

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]