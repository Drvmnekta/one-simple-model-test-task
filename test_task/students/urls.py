"""Module with urls."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from test_task.students.views import StudentsViewSet

router = DefaultRouter()
router.register('students', StudentsViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
