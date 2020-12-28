from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):

    class SubjectName(models.TextChoices):
        MATH = 'MATH', _('MATH')
        ENGLISH = 'ENGLISH', _('ENGLISH')
        HISTORY = 'HISTORY', _('HISTORY')
    subject_name = models.CharField(
        max_length=30,
        choices=SubjectName.choices,
        default=SubjectName.MATH,
        help_text='과목',
    )
    time_table_record = models.ForeignKey(
        'time_tables.TimeTableRecord',
        related_name='time_table_record_subjects',
        on_delete=models.SET_NULL,
        null=True,
        help_text='단위시간표',
    )
    teacher = models.ManyToManyField(
        'time_tables.Teacher',
        related_name='teacher_subjects',
    )

