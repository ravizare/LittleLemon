from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Updated MenuItem Model to match your course requirements
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Changed to precise DecimalField
    inventory = models.SmallIntegerField()  # Added inventory column tracking

    # CHANGED: Updated this method to return the formatted string for your test
    def __str__(self):
        return f"{self.title} : {str(self.price)}"

    # Course method to return formatted item text
    def get_item(self):
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


# --- Token Generation via Signals ---
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
