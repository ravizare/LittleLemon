from django.urls import path
from . import views

urlpatterns = [
    # Updated to match the capitalized class names and added .as_view()
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('booking/', views.BookingView.as_view(), name='booking'),
]
