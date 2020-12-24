from django.db import models


class StudyRoom(models.Model):
    name = models.CharField(max_length=30, help_text='반이름')
    homeroom_teacher = models.OneToOneField(
        'time_tables.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        help_text='담임선생님'
    )
    time_table = models.OneToOneField(
        'time_tables.TimeTable',
        on_delete=models.SET_NULL,
        null=True,
        help_text='시간'
    )

    def __str__(self):
        return self.name