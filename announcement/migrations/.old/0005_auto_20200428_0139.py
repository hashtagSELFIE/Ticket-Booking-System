# Generated by Django 3.0.3 on 2020-04-27 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200427_2304'),
        ('announcement', '0004_auto_20200428_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcer_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Announcer'),
        ),
    ]
