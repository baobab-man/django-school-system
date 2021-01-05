from django.db.models import Q
from django.test import TestCase
from time_tables.models import Subject, StudyRoom, TimeTable, Teacher
from time_tables.tests.test_study_rooms import create_study_rooms
from time_tables.tests.test_subjects import create_subjects
from time_tables.tests.test_teachers import create_teachers
from time_tables.tests.test_time_tables import create_time_tables


def create_teachers_by_subjects(new_teachers_count, subject_multiple_count):
    # teacher1 ~ teacherN 생성
    create_teachers(new_teachers_count)
    teacher_last_id = Teacher.objects.last().id
    teacher_first_id = teacher_last_id - new_teachers_count + 1
    teacher_query = Q(id__gte=teacher_first_id)
    teacher_query &= Q(id__lte=teacher_last_id)
    teachers = list(Teacher.objects.filter(teacher_query).values_list('name', flat=True))
    # (MATH, ENGLISH, HISTORY) * M 생성
    create_subjects(subject_multiple_count)
    subject_last_id = Subject.objects.last().id
    subject_first_id = subject_last_id - (3 * subject_multiple_count) + 1
    subject_query = Q(id__gte=subject_first_id)
    subject_query &= Q(id__lte=subject_last_id)
    subjects = list(Subject.objects.filter(subject_query).values_list('name', flat=True))
    # 두 리스트 묶어서 추출
    item_list_teachers_by_subjects = \
        {teacher: subject for teacher, subject in zip(teachers, subjects)}
    teachers_by_subjects = item_list_teachers_by_subjects.items()
    for teacher_by_subject in teachers_by_subjects:
        return teacher_by_subject


def create_time_tables_by_study_rooms(new_time_tables_count, new_study_rooms_count):
    # time table N개 생성
    create_time_tables(new_time_tables_count)
    time_table_last_id = TimeTable.objects.last().id
    time_table_first_id = time_table_last_id - new_time_tables_count + 1
    time_table_query = Q(id__gte=time_table_first_id) & Q(id__lte=time_table_last_id)
    time_tables = list(TimeTable.objects.filter(time_table_query).values_list('name', flat=True))
    # study room M개 생성
    create_study_rooms(new_study_rooms_count)
    study_room_last_id = StudyRoom.objects.last().id
    study_room_first_id = study_room_last_id - new_study_rooms_count + 1
    study_room_query = Q(id__gte=study_room_first_id) & Q(id__lte=study_room_last_id)
    study_rooms = list(StudyRoom.objects.filter(study_room_query).values_list('name', flat=True))
    # 두 리스트 묶어서 추출
    item_list_time_tables_by_study_rooms = \
        {study_room: time_table for study_room, time_table in zip(study_rooms, time_tables)}
    time_tables_by_study_rooms = item_list_time_tables_by_study_rooms.items()
    for time_table_by_study_room in time_tables_by_study_rooms:
        return time_table_by_study_room


class TestScenarios(TestCase):

    def test_create_teachers_by_subjects(self):
        teacher_count_x = create_teachers_by_subjects(
            new_teachers_count=19,
            subject_multiple_count=3
        )
        teacher_count_y = create_teachers_by_subjects(
            new_teachers_count=22,
            subject_multiple_count=3
        )
        self.assertEqual(teacher_count_x, teacher_count_y)

    def test_create_time_tables_by_study_rooms(self):
        time_table_by_study_room_ex1 = create_time_tables_by_study_rooms(
            new_time_tables_count=3,
            new_study_rooms_count=2
        )
        time_table_by_study_room_ex2 = create_time_tables_by_study_rooms(
            new_time_tables_count=2,
            new_study_rooms_count=7
        )
        self.assertEqual(time_table_by_study_room_ex1, time_table_by_study_room_ex2)
