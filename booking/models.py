from django.db import models
from account.models import Account
from schedule.models import Train, Timetable, Station


# Create your models here.
class Ticket(models.Model):
    buyer = models.ForeignKey(Account, on_delete=models.CASCADE)
    boardingTrain = models.ForeignKey(Train, on_delete=models.CASCADE)
    fromStation = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, related_name="fromStation")
    toStation = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, related_name="toStation")
    transactionInformation = models.TextField(default='')
    transactionStatus = models.BooleanField(default=False)
    buyDate = models.DateField(auto_now_add=True)
    bookingStatus = models.BooleanField(default=False)
