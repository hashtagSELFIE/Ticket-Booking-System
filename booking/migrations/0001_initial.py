# Generated by Django 3.0.5 on 2020-04-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
    ]