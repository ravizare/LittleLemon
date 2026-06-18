from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# 1. Index / Home View
def index(request):
    return render(request, 'index.html', {})

# 2. About View
def about(request):
    return render(request, 'about.html', {})

# 3. Book / Reservation View
def book(request):
    return render(request, 'book.html', {})

# 4. Menu View
def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_data})

# 5. Say Hello View (API/Text test)
def sayHello(request):
    return HttpResponse('Hello World')

# Add this to the bottom of your reservation/views.py file

def display_menu_item(request, pk=None):
    if pk:
        # Tries to find the specific menu item by its primary key (ID)
        try:
            item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            item = None
    else:
        item = ""
    return render(request, 'menu_item.html', {"menu_item": item})