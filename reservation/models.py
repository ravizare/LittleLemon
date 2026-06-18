from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    Price = models.IntegerField(default=0)      # Added default=0
    Inventory = models.IntegerField(default=0)  # Added default=0
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name