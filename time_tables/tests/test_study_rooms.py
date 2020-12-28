from django.test import TestCase
from time_tables.models import StudyRoom


def create_study_rooms():
    study_rooms = []
    for i in range(1, 3):
        study_room_name = 'study_room' + str(i)
        study_room = StudyRoom(
            name=study_room_name,
        )
        study_rooms.append(study_room)
    StudyRoom.objects.bulk_create(study_rooms)


class TestStudyRooms(TestCase):

    def test_create_study_rooms(self):
        create_study_rooms()
        study_rooms = StudyRoom.objects.all()
        for study_room in study_rooms:
            print(study_room)
