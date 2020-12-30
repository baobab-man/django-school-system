from django.test import TestCase
from time_tables.models import TimeTable


def create_time_tables():
    time_tables = []
    for i in range(1, 4):
        time_table_name = 'period' + str(i)
        time_table = TimeTable(
            name=time_table_name,
        )
        time_tables.append(time_table)
    TimeTable.objects.bulk_create(time_tables)


class TestTimeTables(TestCase):

    def test_create_time_tables(self):
        create_time_tables()
        time_tables = TimeTable.objects.all()
        for time_table in time_tables:
            print(time_table)