from django.db import models


class Subject(models.Model):
    MATH = 'MATH'
    ENGLISH = 'ENGLISH'
    HISTORY = 'HISTORY'
    SUBJECT_CHOICES = (
        (MATH, 'MATH'),
        (ENGLISH, 'ENGLISH'),
        (HISTORY, 'HISTORY'),
    )
    name = models.CharField(
        max_length=30,
        choices=SUBJECT_CHOICES,
        help_text='과목'
    )
    time_table = models.ForeignKey(
        'time_tables.TimeTable',
        related_name='time_table_subjects',
        on_delete=models.SET_NULL,
        null=True,
        help_text='과'
    )
    teacher = models.ManyToManyField(
        'time_tables.Teacher',
        related_name='teacher_subjects',
    )

