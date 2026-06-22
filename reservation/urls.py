from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # 1. Menu item list and detail endpoints
    path('menu-items/', views.MenuItemsView.as_view(), name='menu_items_list'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item_detail'),
    
    # 2. Token-protected message endpoint
    path('message/', views.msg, name='protected_message'),
    
    # 3. Secure token retrieval endpoint (Resolves to /api/api-token-auth/)
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
