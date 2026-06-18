from django.urls import path
from . import views

urlpatterns = [
    # Clean paths for your generic menu views
    path('menu/items', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('msg/', views.securedview, name='secured_msg'), 
]
