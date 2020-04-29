from django.db import models
from account.models import Announcer


# Create your models here.
class Announcement(models.Model):
    announcer_user = models.ForeignKey(
        Announcer, on_delete=models.CASCADE, null=True)
    announce_text = models.TextField()
    announce_time = models.DateTimeField()
