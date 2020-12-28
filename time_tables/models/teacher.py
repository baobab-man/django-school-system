from django.db import models


class Teacher(models.Model):
    name = models.CharField(
        max_length=30,
        help_text='선생님'
    )
