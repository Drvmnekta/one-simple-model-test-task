"""Module with admin panel configuration."""

from django.contrib import admin

from test_task.students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Class for admin panel of students objects."""
    
    list_display = (
        'name', 'age', 'department'
    )
    search_fields = (
        'name', 'age', 'department'
    )
    empty_value_display = '-empty-'
