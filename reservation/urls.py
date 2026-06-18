from django.urls import path
from . import views

urlpatterns = [
    path('menu/items', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    
    # Add this line to wire up your secured endpoint:
    path('msg/', views.securedview, name='secured_msg'), 
]
