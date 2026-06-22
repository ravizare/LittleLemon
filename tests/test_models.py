from django.test import TestCase
# Replace 'restaurant' with your actual Django app name if it is different
from reservation.models import MenuItem 

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Creates a temporary test instance in the test database
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        
        # Validates if the __str__ method matches the expected output
        self.assertEqual(str(item), "IceCream : 80")
