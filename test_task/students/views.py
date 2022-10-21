"""Module with views."""

from test_task.students.mixins import CreateListViewSet
from test_task.students.models import Student
from test_task.students.serializers import StudentSerializer


class StudentsViewSet(CreateListViewSet):
    """Viewset for students."""
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
