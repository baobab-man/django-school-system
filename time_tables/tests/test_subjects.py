from django.test import TestCase
from time_tables.models import Subject


def create_subjects():
    subject_choices = Subject.SubjectName.choices
    subject_names = [choice[1] for choice in subject_choices]
    print(subject_names)


class TestSubjects(TestCase):

    def test_create_subjects(self, subjects=None):
        create_subjects()
        # subjects = Subject.objects.all()
        for subject in subjects:
            print(subject)

    def test_subjects(self):
        subject_names = create_subjects()
        return subject_names


