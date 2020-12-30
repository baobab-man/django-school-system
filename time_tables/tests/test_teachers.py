from django.test import TestCase
from time_tables.models import Teacher


def create_teachers(start, end):
    teachers = []
    for i in range(start, end + 1):
        teacher_name = 'teacher' + str(i)
        teacher = Teacher(
            name=teacher_name
        )
        teachers.append(teacher)
    print(Teacher.objects.bulk_create(teachers))


class TestTeachers(TestCase):

    def test_create_teachers(self):
        return create_teachers(1, 10)
        # teachers = Teacher.objects.all()
        # for teacher in teachers:
        #     print(teacher)
