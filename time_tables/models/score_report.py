from django.db import models


class ScoreReport(models.Model):
    student = models.OneToOneField(
        'time_tables.Student',
        on_delete=models.SET_NULL,
        null=True,
        help_text='학생'
    )
    score = models.IntegerField(
        help_text='점',
        default=0
    )
