from django.db import models


class TimeTable(models.Model):
    period = models.IntegerField(help_text='교시')
    DAY_OF_WEEK_CHOICES = (
        ('MON', 'MON'),
        ('TUE', 'TUE'),
        ('WED', 'WED'),
        ('THU', 'THU'),
        ('FRI', 'FRI')
    )
    day_of_week = models.CharField(max_length=30, help_text='요일')

