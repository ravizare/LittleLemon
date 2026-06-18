from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets  # Added 'viewsets' here

# Built-in User model and its serializer imports
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Your existing model and serializer imports
from .models import Menu, Booking  
from .serializers import BookingSerializer, MenuSerializer  

# --- 1. User ViewSet for the DefaultRouter ---
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# --- 2. Your Existing API Views ---
class BookingView(APIView):

    def get(self, request):
         items = Booking.objects.all()  
         serializer = BookingSerializer(items, many=True)
         return Response(serializer.data)

class MenuView(APIView):

    def post(self, request):
         serializer = MenuSerializer(data=request.data)

         if serializer.is_valid():
              serializer.save()
              return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
         
         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
