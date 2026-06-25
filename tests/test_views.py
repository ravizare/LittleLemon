from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        # 1. Initialize the REST Framework test client
        self.client = APIClient()

        # 2. Create a test user and generate an auth token
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.get(
            user=self.user
        )  # Your models.py signal automatically creates this!

        # 3. Authenticate the test client using the token
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        # 4. Create test instances of the MenuItem model
        self.item1 = MenuItem.objects.create(
            title="Pizza", price=12.00, inventory=50
        )
        self.item2 = MenuItem.objects.create(
            title="Burger", price=8.50, inventory=30
        )
        self.item3 = MenuItem.objects.create(
            title="Salad", price=7.00, inventory=20
        )

    def test_getall(self):
        # Make the authorized request
        url = reverse("menu_items_list")
        response = self.client.get(url)

        # Fetch data from test database and serialize it
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
