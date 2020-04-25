from django.db import models
from account.models import Account
from schedule.models import Timetable


# Create your models here.

class Ticket(models.Model):
    buyer = models.ForeignKey(Account, on_delete=models.CASCADE)
    boardingTrain = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    transactionInformation = models.TextField()
    transactionStatus = models.BooleanField()
    buyDate = models.DateField()
    bookingStatus = models.BooleanField()
