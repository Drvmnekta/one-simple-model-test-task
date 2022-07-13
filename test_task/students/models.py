from django.core.validators import MaxValueValidator
from django.db import models

BIOLOGY = 'bio'
MATHS = 'math'
ECONOMICS = 'eco'

DEPARTMENTS = [
    (BIOLOGY, 'Биология'),
    (MATHS, 'Математика'),
    (ECONOMICS, 'Экономика'),
]


class Student(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя',
    )
    age = models.IntegerField(
        validators=[MaxValueValidator(100)],
        verbose_name='Возраст',
    )
    department = models.CharField(
        choices=DEPARTMENTS,
        default='eco',
        blank=False,
        null=False,
        max_length=100,
        verbose_name='Кафедра',
    )
