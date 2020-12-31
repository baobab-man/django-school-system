from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeTableRecord(models.Model):

    class DayOfWeek(models.TextChoices):
        MON = 'MON', _('MON')
        TUE = 'TUE', _('TUE')
        WED = 'WED', _('WED')
        THU = 'THU', _('THU')
        FRI = 'FRI', _('FRI')
    period = models.IntegerField(
        help_text='교시',
        default=1,
    )
    day_of_week = models.CharField(
        max_length=30,
        choices=DayOfWeek.choices,
        default=DayOfWeek.MON,
        help_text='요일',
    )
    time_table = models.ForeignKey(
        'time_tables.TimeTable',
        related_name='time_table_time_table_records',
        on_delete=models.SET_NULL,
        null=True,
        help_text='시간표',
    )
    subject = models.ForeignKey(
        'time_tables.Subject',
        related_name='subjects_time_table_record',
        on_delete=models.SET_NULL,
        null=True,
        help_text='과목',
    )
    teacher = models.ForeignKey(
        'time_tables.Teacher',
        related_name='teacher_time_table_records',
        on_delete=models.SET_NULL,
        null=True,
        help_text='선생님',
    )
