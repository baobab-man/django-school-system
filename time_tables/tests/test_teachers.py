from django.test import TestCase
from time_tables.models import Teacher


def create_teachers():
    teachers = []
    for i in range(1, 11):
        teacher_name = 'teacher' + str(i)
        teacher = Teacher(
            name=teacher_name
        )
        teachers.append(teacher)
    Teacher.objects.bulk_create(teachers)


class TestTeachers(TestCase):

    def test_create_teachers(self):
        create_teachers()
        teachers = Teacher.objects.all()
        for teacher in teachers:
            print(teacher)
