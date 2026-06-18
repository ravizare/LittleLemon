from django.contrib import admin
# Changed Menu to MenuItem to match your new models.py file
from .models import MenuItem, Booking  

admin.site.register(Booking)
# Update the register line to use MenuItem as well
admin.site.register(MenuItem)  
