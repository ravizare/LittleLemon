from rest_framework import viewsets, generics, permissions  # 1. Added 'permissions' here
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MenuItem, Booking  
from .serializers import UserSerializer, BookingSerializer, MenuItemSerializer  

# --- 1. User ViewSet for the DefaultRouter ---
# Added right here at the top of your view classes
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all() 
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] # Restricts access to logged-in users only

# --- 2. Booking ViewSet for the Tables Router ---
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# --- 3. Menu Items Views using DRF Generics ---
class MenuItemsView(generics.ListCreateAPIView): 
    queryset = MenuItem.objects.all() 
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):     
    queryset = MenuItem.objects.all() 
    serializer_class = MenuItemSerializer
