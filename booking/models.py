from django.db import models


# Create your models here.

class Ticket(models.Model):
    # buyer = models.ForeignKey('', on_delete=models.CASCADE)
    # boardingTrain = models.ForeignKey('', on_delete=models.CASCADE)
    transactionInformation = models.TextField()
    transactionStatus = models.BooleanField()
    buyDate = models.DateField()
    bookingStatus = models.BooleanField()
