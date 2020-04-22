from django.db import models

# Create your models here.

class Account(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    gender = models.TextField()
    birthdate = models.DateField()
    userType = models.TextField()