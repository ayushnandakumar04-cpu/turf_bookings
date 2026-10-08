from django.db import models

from turf_management.models import Turf

# Create your models here.

class TurfRegister(models.Model):

    team_name = models.CharField(max_length=200)

    phone_number = models.PositiveIntegerField()

    date = models.DateField()

    duration = models.CharField(max_length=150)

    def __str__(self):

        return self.team_name
