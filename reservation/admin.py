from django.contrib import admin
# Change 'menu, booking' to capital letters 'Menu, Booking'
from .models import Menu, Booking 

admin.site.register(Booking)
admin.site.register(Menu)
