"""Module with serializers."""

from rest_framework import serializers

from test_task.students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer of student model."""

    class Meta:
        """Meta class of serializer."""
        
        model = Student
        fields = '__all__'
