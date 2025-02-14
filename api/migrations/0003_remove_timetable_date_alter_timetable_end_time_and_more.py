# Generated by Django 5.1.6 on 2025-02-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='date',
        ),
        migrations.AlterField(
            model_name='timetable',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
