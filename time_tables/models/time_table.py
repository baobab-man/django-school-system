from django.db import models


class TimeTable(models.Model):
    study_room = models.OneToOneField(
        'time_tables.StudyRoom',
        on_delete=models.SET_NULL,
        null=True,
        help_text='반'
    )

