# Generated by Django 3.0.5 on 2020-04-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20200424_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='train_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.Train'),
        ),
    ]