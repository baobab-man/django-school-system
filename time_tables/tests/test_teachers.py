from django.test import TestCase
from time_tables.models import Teacher


def create_teacher():
    teacher_name = 'teacher'
    teacher = Teacher.objects.create(
        name=teacher_name
    )
    return teacher


def create_teachers(teachers_count):
    teachers = []
    for i in range(teachers_count):
        teacher_name = 'teacher' + str(i+1)
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
        create_teachers(10)
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 10)
