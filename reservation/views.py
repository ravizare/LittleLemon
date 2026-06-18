from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Imported for clean HTTP responses

# 1. Capitalised Menu and Booking to match models.py
from .models import Menu, Booking  
# 2. Capitalised MenuSerializer to match standard naming
from .serializers import BookingSerializer, MenuSerializer  

class BookingView(APIView):  # Capitalised class name following Python standards

    def get(self, request):
         # 3. Changed lowercase booking to capital Booking
         items = Booking.objects.all()  
         serializer = BookingSerializer(items, many=True)
         return Response(serializer.data)  # Return JSON

class MenuView(APIView):  # Capitalised class name following Python standards

    def post(self, request):
         # 4. Changed lowercase menuSerializer to MenuSerializer
         serializer = MenuSerializer(data=request.data)

         if serializer.is_valid():
              serializer.save()
              return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
         
         # 5. Added an error return if the incoming data is invalid
         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
