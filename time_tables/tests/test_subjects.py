from django.test import TestCase
from time_tables.models import Subject


def create_subject(time_table_record=None, teacher=None):
    subject_name = Subject.SubjectName.choices[0]
    subject = Subject.objects.create(
        subject_name=subject_name,
        time_table_record=time_table_record,
    )
    if teacher:
        subject.teachers.add(teacher)
    return subject


def create_subjects(time_table_record=None, teacher=None):
    subjects = []
    subject_choices = Subject.SubjectName.choices
    subject_names = [choice[0] for choice in subject_choices]
    for subject_name in subject_names:
        subject = Subject(
            subject_name=subject_name,
            time_table_record=time_table_record,
        )
        if teacher:
            subject.teachers.add(teacher)
        subjects.append(subject)
    Subject.objects.bulk_create(subjects)


class TestSubjects(TestCase):

    def test_create_subject(self):
        subject = create_subject()
        self.assertNotEqual(subject, None)

    def test_create_subjects(self):
        before_subject_count = Subject.objects.all().count()
        new_subject_count = len(Subject.SubjectName.choices)
        create_subjects()
        subjects = Subject.objects.all()
        expected_subject_count = before_subject_count + new_subject_count
        self.assertEqual(subjects.count(), expected_subject_count)


