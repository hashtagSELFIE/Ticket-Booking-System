from django.db import models

# Create your models here.

class Schedule(models.Model):
    trainName = models.TextField()
    trainType = models.TextField()
    arrivedTime = models.DateTimeField()
    departedTime = models.DateTimeField()
    fromStation = models.TextField()
    toStation = models.TextField()