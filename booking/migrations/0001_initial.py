# Generated by Django 3.0.5 on 2020-04-28 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('schedule', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionInformation', models.TextField()),
                ('transactionStatus', models.BooleanField()),
                ('buyDate', models.DateField()),
                ('bookingStatus', models.BooleanField()),
                ('boardingTrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Timetable')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
    ]
