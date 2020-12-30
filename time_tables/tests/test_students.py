from django.test import TestCase
from time_tables.models import Student, StudyRoom
from time_tables.tests.test_study_rooms import create_study_room


def create_student(study_room=None):
    student_name = 'student'
    student = Student.objects.create(
        name=student_name,
        study_room=study_room,
    )
    return student


def create_students(start, end, study_room=None):
    students = []
    for i in range(start, end + 1):
        student_name = 'student' + str(i)
        student = Student(
            name=student_name,
            study_room=study_room,
        )
        students.append(student)
    Student.objects.bulk_create(students)


class TestStudents(TestCase):
    def test_create_student(self):
        study_room = create_study_room()
        student = create_student(study_room)
        self.assertNotEqual(student, None)

    def test_create_students(self):
        before_student_count = Student.objects.all().count()
        new_student_count = 50
        create_students(1, new_student_count, study_room=create_study_room())
        students = Student.objects.all()
        expected_student_count = before_student_count + new_student_count
        self.assertEqual(students.count(), expected_student_count)
