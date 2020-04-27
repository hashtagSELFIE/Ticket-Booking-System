from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from schedule.models import Station
from .utils import GenderTypes


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
    gender = models.IntegerField(
        choices=GenderTypes.choices(),
        default=GenderTypes.PREFER,
    )
    birth_date = models.DateField(blank=True, null=True)
    user_type = models.TextField(
        choices=userType,
        default=USER
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_fullname(self):
        return self.user_id.first_name + self.user_id.last_name

    def get_gender_label(self):
        return GenderTypes(self.gender).name.title()


class Announcer(models.Model):
    user = models.OneToOneField(
        Account, primary_key=True, on_delete=models.CASCADE)


class TicketSeller(models.Model):
    user = models.OneToOneField(
        Account, primary_key=True, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def create_user_arofile(sender, instance, created, **kwargs):
#     if created:
#         Account.objects.create(user_id=instance)


# @receiver(post_save, sender=User)
# def save_user_account(sender, instance, **kwargs):
#     account = Account.objects.get(user_id=instance)
#     if account:
#         account.save()
#     else:
#         account = Account.objects.create(user_id=instance)
#         account.save()
