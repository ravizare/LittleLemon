from django.db import models

class MenuItem(models.Model):
   title = models.CharField(max_length=100) # You can use 'title' or 'item'
   price = models.IntegerField()

   def __str__(self):
       return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
