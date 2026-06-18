from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response  # Needed for your securedview to work
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import MenuItem, Booking  
from .serializers import UserSerializer, BookingSerializer, MenuItemSerializer  

# --- 1. User ViewSet for the DefaultRouter ---
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

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

# --- 4. Secured View (Function-Based View with Token/Session Authentication) ---
# Look at the bottom of your reservation/views.py and ensure it looks like this:

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})
