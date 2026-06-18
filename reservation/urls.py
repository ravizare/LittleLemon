from django.urls import path
from . import views

urlpatterns = [
    # 1. Matches the required endpoints for your Generic views
    path('menu-items/', views.MenuItemsView.as_view(), name='menu_items_list'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item_detail'),
    
    # 2. Re-routed your function-based message view to the requested endpoint path
    path('message/', views.msg, name='protected_message'),
]
