from django.test import TestCase

from time_tables.models import Student
from time_tables.models import StudyRoom


class TestStudents(TestCase):

    def create_students(self):
        students = []
        for i in range(50):
            student_name = 'student' + str(i)
            student = Student(
                name=student_name,
            )
            students.append(student)
        Student.objects.bulk_create(students)

    def create_study_rooms(self):
        study_rooms = []
        for i in range(2):
            study_room_name = 'study_room' + str(i)
            study_room = StudyRoom(
                name=study_room_name,
            )
            study_rooms.append(study_room)
        StudyRoom.objects.bulk_create(study_rooms)

    def test_create_student(self):
        self.create_students()
        students = Student.objects.all()
        for student in students:
            print(student)

    def test_create_study_room(self):
        self.create_study_rooms()
        study_rooms = StudyRoom.objects.all()
        for study_room in study_rooms:
            print(study_room)

    # def test_separate_students(self):
    #     study_room_name = StudyRoom.objects.test_create_study_room()
    #     if study_room_name == 'study_room' + str(1):
    #         for separate_students in
