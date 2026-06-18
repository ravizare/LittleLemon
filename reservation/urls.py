from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]



from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'),
    path('', views.index, name='index') 
]