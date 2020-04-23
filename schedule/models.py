from django.db import models


# Create your models here.


class Station(models.Model):
    station_name = models.TextField()


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
    train_name = models.OneToOneField(Train, on_delete=models.CASCADE, primary_key=True)
    train_type = models.TextField()
    arrived_time = models.DateTimeField()
    departed_time = models.DateTimeField()
    from_station = models.TextField()
    to_station = models.TextField()
