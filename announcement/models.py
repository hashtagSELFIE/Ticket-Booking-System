from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Announcer(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

class Announcement(models.Model):
    announcer_user = models.ForeignKey(Announcer, on_delete=models.CASCADE)
    announce_text = models.TextField()
    announce_time = models.DateTimeField()
