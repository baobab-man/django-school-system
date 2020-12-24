# Generated by Django 3.1.4 on 2020-12-23 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(help_text='학생이름', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_room',
            field=models.ForeignKey(help_text='반', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='study_room_students', to='time_tables.studyroom'),
        ),
        migrations.AlterField(
            model_name='studyroom',
            name='homeroom_teacher',
            field=models.OneToOneField(help_text='담임선생님', null=True, on_delete=django.db.models.deletion.SET_NULL, to='time_tables.teacher'),
        ),
        migrations.AlterField(
            model_name='studyroom',
            name='name',
            field=models.CharField(help_text='반이름', max_length=30),
        ),
        migrations.AlterField(
            model_name='studyroom',
            name='time_table',
            field=models.OneToOneField(help_text='시간', null=True, on_delete=django.db.models.deletion.SET_NULL, to='time_tables.timetable'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(help_text='선생님', max_length=30),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day_of_week',
            field=models.CharField(help_text='요일', max_length=30),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='period',
            field=models.IntegerField(help_text='교시'),
        ),
    ]