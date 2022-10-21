"""Module with models."""

from django.core.validators import MaxValueValidator
from django.db import models

BIOLOGY = 'bio'
MATHS = 'math'
ECONOMICS = 'eco'

departments = [
    (BIOLOGY, 'Биология'),
    (MATHS, 'Математика'),
    (ECONOMICS, 'Экономика'),
]


class Student(models.Model):
    """Model of student."""
    
    name = models.CharField(
        max_length=100,
        verbose_name='Имя',
    )
    age = models.IntegerField(
        validators=[MaxValueValidator(100)],
        verbose_name='Возраст',
    )
    department = models.CharField(
        choices=departments,
        default='eco',
        blank=False,
        null=False,
        max_length=100,
        verbose_name='Кафедра',
    )
