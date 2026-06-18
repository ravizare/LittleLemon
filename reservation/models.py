from django.db import models

# Changed "menu" to "Menu" with a capital M to fix the import errors
class Menu(models.Model):
   item = models.CharField(max_length=100)
   price = models.IntegerField()

   def __str__(self):
       return self.item

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
