from django.db import models

# Create your models here.


class Passenger(models.Model):
    Name = models.CharField(25)
    Gender = models.CharField(10)
    Survived = models.BooleanField(default=True)
    Age = models.FloatField()
    ticket_classes = models.PositiveSmallIntegerField()
    embarked = models.CharField(40)