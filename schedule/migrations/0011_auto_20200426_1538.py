# Generated by Django 3.0.5 on 2020-04-26 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20200424_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='station_id',
            new_name='station',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='train_name',
            new_name='train',
        ),
    ]
