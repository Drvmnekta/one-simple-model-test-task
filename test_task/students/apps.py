"""Module of app config."""

from django.apps import AppConfig


class StudentsConfig(AppConfig):
    """Students app config class."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
