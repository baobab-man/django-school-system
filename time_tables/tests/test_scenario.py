from django.db.models import Q
from django.test import TestCase
from time_tables.models import Subject, StudyRoom, Student, TimeTableRecord, TimeTable, Teacher
from time_tables.tests.test_subjects import create_subjects
from time_tables.tests.test_teachers import create_teachers


def create_teachers_by_subjects(new_teachers_count, subject_multiple_count):
    # teacher1 ~ teacherN 생성
    create_teachers(new_teachers_count)
    teacher_last_id = Teacher.objects.last().id
    teacher_first_id = teacher_last_id - new_teachers_count + 1
    teacher_query = Q(id__gte=teacher_first_id) & Q(id__lte=teacher_last_id)
    teachers = list(Teacher.objects.filter(teacher_query).values_list('name', flat=True))
    # (MATH, ENGLISH, HISTORY) * M 생성
    create_subjects(subject_multiple_count)
    subject_last_id = Subject.objects.last().id
    subject_first_id = subject_last_id - (3 * subject_multiple_count) + 1
    subject_query = Q(id__gte=subject_first_id) & Q(id__lte=subject_last_id)
    subjects = list(Subject.objects.filter(subject_query).values_list('name', flat=True))

    item_list_teachers_by_subjects = \
        {teacher: subject for teacher, subject in zip(teachers, subjects)}
    teachers_by_subjects = item_list_teachers_by_subjects.items()
    for teacher_by_subject in teachers_by_subjects:
        return teacher_by_subject


class TestScenarios(TestCase):

    def test_create_teacher_by_subject(self):
        teacher_count_x = create_teachers_by_subjects(
            new_teachers_count=19,
            subject_multiple_count=3
        )
        teacher_count_y = create_teachers_by_subjects(
            new_teachers_count=22,
            subject_multiple_count=3
        )
        self.assertEqual(teacher_count_x, teacher_count_y)
