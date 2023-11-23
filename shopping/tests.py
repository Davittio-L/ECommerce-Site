from django.test import TestCase, Client
from django.urls import reverse
from .models import Product  # Import your Product model

class StoreViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some test product data
        Product.objects.create(name='Test Product 1', price=100.00)
        Product.objects.create(name='Test Product 2', price=200.00)

    def test_store_view(self):
        # Simulate a GET request
        response = self.client.get(reverse('store'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'shopping/store.html')

        # Check that the context contains the correct data
        self.assertTrue('products' in response.context)
        self.assertTrue('cartItems' in response.context)

        # Optionally, check the contents of the context
        products_in_context = response.context['products']
        self.assertEqual(products_in_context.count(), 2) 