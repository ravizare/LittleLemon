from rest_framework import serializers
from django.contrib.auth.models import User  # Imported the built-in User model
from .models import Booking, Menu  

# New UserSerializer class to serialize the User model instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups'] # Specifies the fields to be exposed via the API

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
