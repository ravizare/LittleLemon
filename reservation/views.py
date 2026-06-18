from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MenuItem, Booking  
from .serializers import UserSerializer, BookingSerializer, MenuItemSerializer  

# --- 1. User ViewSet for the DefaultRouter ---
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# --- 2. Step 3: Booking ViewSet (Replaced the old BookingView) ---
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
