from django.test import TestCase
from time_tables.models import Student, StudyRoom


def create_students(study_room=None):
    students = []
    for i in range(1, 51):
        student_name = 'student' + str(i)
        student = Student(
            name=student_name,
            study_room=study_room
        )
        students.append(student)
    Student.objects.bulk_create(students)


class TestStudents(TestCase):

    def test_create_students(self):
        create_students()
        students = Student.objects.all()
        # study_rooms = StudyRoom.objects.all()
        # student_count = 20

        for student in students:
            # start = 1 + student_count * (study_room.id - 1)
            # end = student_count * study_room.id + 1
            # # create_students(start, end, study_room)
            # for student in create_students(start, end, study_room):
            print(student)
