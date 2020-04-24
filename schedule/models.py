from django.db import models


# Create your models here.


class Station(models.Model):
    station_name = models.TextField()
    english_station_name = models.TextField(null=True)


class Train(models.Model):
    EXPRESS = 'EX'
    LOCAL = 'LC'
    train_name = models.TextField()
    trainType = (
        (EXPRESS, "Express"),
        (LOCAL, "Local")
    )
    train_type = models.TextField(
        choices=trainType,
        default=LOCAL
    )
    amount_of_passenger = models.IntegerField(null=True)


class Timetable(models.Model):
    train_name = models.OneToOneField(Train, on_delete=models.CASCADE)
    station_id = models.OneToOneField(Station, on_delete=models.CASCADE, default=None, null=True)
    arrived_time = models.TimeField()
    departed_time = models.TimeField()
