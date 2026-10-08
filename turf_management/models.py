from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Turf(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    email = models.EmailField()

    phone_number = models.PositiveIntegerField()