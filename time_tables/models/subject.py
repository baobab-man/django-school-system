from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):

    class SubjectName(models.TextChoices):
        MATH = 'MATH', _('MATH')
        ENGLISH = 'ENGLISH', _('ENGLISH')
        HISTORY = 'HISTORY', _('HISTORY')
    name = models.CharField(
        max_length=30,
        choices=SubjectName.choices,
        default=SubjectName.MATH,
        help_text='과목',
    )
    teachers = models.ManyToManyField(
        'time_tables.Teacher',
        related_name='teacher_subjects',
    )

    def __str__(self):
        return self.name
