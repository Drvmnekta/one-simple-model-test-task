from .mixins import CreateListViewSet
from .models import Student
from .serializers import StudentSerializer


class StudentsViewSet(CreateListViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
