from django.test import TestCase
from time_tables.models import Teacher


def create_teacher():
    teacher_name = 'teacher'
    teacher = Teacher.objects.create(
        name=teacher_name
    )
    return teacher


def create_teachers(start, end):
    teachers = []
    for i in range(start, end + 1):
        teacher_name = 'teacher' + str(i)
        teacher = Teacher(
            name=teacher_name
        )
        teachers.append(teacher)
    Teacher.objects.bulk_create(teachers)


class TestTeachers(TestCase):

    def test_create_teacher(self):
        teacher = create_teacher()
        self.assertNotEqual(teacher, None)

    def test_create_teachers(self):
        create_teachers(1, 10)
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 10)
