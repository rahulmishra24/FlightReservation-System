from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Flights(models.Model):
    flightNumber = models.IntegerField()
    departureCity = models.CharField(max_length = 10)
    arrivalCity = models.CharField(max_length = 10)
    departureDate = models.DateField()
    estimatedTime = models.TimeField()

# class Passenger(models.Model):
#     name = models.CharField(max_length = 10)
#     address = models.CharField(max_length = 20)
#     contact = models.IntegerField(max_length = 10)
#     gender = models.CharField(max_length = 5)

class Reservation(models.Model):
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
