from rest_framework import serializers
# 1. Imported both Booking and Menu from your models
from .models import Booking, Menu  

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# 2. Added MenuSerializer to handle menu POST requests from views.py
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
