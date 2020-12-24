from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=30)
    time_table = models.ForeignKey(
        'time_tables.TimeTable',
        related_name='time_table_subjects',
        on_delete=models.SET_NULL,
        null=True
    )
    teacher = models.ManyToManyField(
        'time_tables.Teacher',
        related_name='teacher_subjects',
    )
