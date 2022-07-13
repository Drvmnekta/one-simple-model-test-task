from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'age', 'department'
    )
    search_fields = (
        'name', 'age', 'department'
    )
    empty_value_display = '-empty-'
