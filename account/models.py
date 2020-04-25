from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    USER = 'US'
    SELLER = 'TS'
    ANNOUNCER = 'AN'
    userType = (
        (USER, "Normal User"),
        (SELLER, "Ticket Seller"),
        (ANNOUNCER, "Announcer")
    )

    # first_name = models.TextField()
    # last_name = models.TextField()
    # email = models.TextField()
    gender = models.TextField()
    birth_date = models.DateField()
    user_type = models.TextField(
        choices=userType,
        default=USER
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
