from django.test import TestCase
from time_tables.models import StudyRoom


def create_study_room():
    study_room_name = 'study_room'
    study_room = StudyRoom.objects.create(
        name=study_room_name,
    )
    return study_room


def create_study_rooms(start, end):
    study_rooms = []
    for i in range(start, end + 1):
        study_room_name = 'study_room' + str(i)
        study_room = StudyRoom(
            name=study_room_name,
        )
        study_rooms.append(study_room)
    StudyRoom.objects.bulk_create(study_rooms)


class TestStudyRooms(TestCase):

    def test_create_study_room(self):
        study_room = create_study_room()
        self.assertNotEqual(study_room, None)

    def test_create_study_rooms(self):
        create_study_rooms(1, 2)
        study_rooms = StudyRoom.objects.all()
        self.assertEqual(study_rooms.count(), 2)
