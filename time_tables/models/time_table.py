from django.db import models


class TimeTable(models.Model):
    name = models.CharField(
        max_length=30,
        help_text='시간표명',
        null=True,
    )
    study_room = models.OneToOneField(
        'time_tables.StudyRoom',
        on_delete=models.SET_NULL,
        null=True,
        help_text='반',
    )
