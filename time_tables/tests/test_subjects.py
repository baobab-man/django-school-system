from django.test import TestCase
from time_tables.models import Subject


def create_subject(teacher=None):
    subject_name = Subject.SubjectName.choices[0]
    subject = Subject.objects.create(
        name=subject_name,
    )
    if teacher:
        subject.teachers.add(teacher)
    return subject


def create_subjects(n, teacher=None):
    subjects = []
    subject_choices = Subject.SubjectName.choices
    subject_names = n * [choice[0] for choice in subject_choices]
    for subject_name in subject_names:
        subject = Subject(
            name=subject_name,
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
        create_subjects(1)
        subjects = Subject.objects.all()
        expected_subject_count = before_subject_count + new_subject_count
        self.assertEqual(subjects.count(), expected_subject_count)


