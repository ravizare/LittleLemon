from django.urls import path
from . import views

urlpatterns = [
    # Main Menu View Paths (DRF Generic Views)
    path('menu/items', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
]
