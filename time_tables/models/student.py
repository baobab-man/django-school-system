from django.db import models


class Student(models.Model):
    """
    student 모델
    :field name: Char, 학생이름
    :field study_room: FK, 반
    """
    name = models.CharField(
        max_length=30,
        help_text='학생이름'
    )
    study_room = models.ForeignKey(
        'time_tables.StudyRoom',
        related_name='study_room_students',
        on_delete=models.SET_NULL,
        null=True,
        help_text='반'
    )

    def __str__(self):
        return self.name
