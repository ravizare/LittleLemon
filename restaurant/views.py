from django.contrib.auth.models import User
from django.shortcuts import render  # ADDED: Needed to render your HTML template
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response  # Needed for your securedview to work

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer


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
    permission_classes = [
        IsAuthenticated
    ]  # Enforces token protection for the menu list
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateAPIView, generics.DestroyAPIView
):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# --- 4. Secured View (Function-Based View with Token/Session Authentication) ---
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})


# --- 5. Frontend HTML Template View ---
# ADDED: This view handles serving your new index.html file
def home(request):
    return render(request, "restaurant/index.html")
