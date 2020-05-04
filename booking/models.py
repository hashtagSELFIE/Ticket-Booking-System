from django.db import models
from account.models import Account
from schedule.models import Train, Timetable, Station


# Create your models here.
class Ticket(models.Model):
    buyer = models.ForeignKey(Account, on_delete=models.CASCADE)
    boarding_train = models.ForeignKey(Train, on_delete=models.CASCADE)
    from_station = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, related_name="fromStation")
    to_station = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, related_name="toStation")
    transaction_information = models.TextField(default='')
    transaction_status = models.BooleanField(default=False)
    buy_date = models.DateField(auto_now_add=True)
    travel_date = models.DateField(auto_now_add=True)
    booking_status = models.BooleanField(default=False)
