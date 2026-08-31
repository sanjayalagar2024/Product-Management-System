# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from decimal import Decimal
# from .models import Product

# class DairySimpleTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='admin_test', password='123')
#         self.product = Product.objects.create(
#             name='Milk 500ml',
#             category='Milk',
#             quantity=50,
#             price=Decimal('30.00')
#         )

#     def test_product_str(self):
#         self.assertEqual(str(self.product), "Milk 500ml - ₹30.00")

#     def test_login_and_dashboard(self):
#         # Unauthenticated redirects to login
#         res = self.client.get(reverse('dashboard'))
#         self.assertEqual(res.status_code, 302)

#         # Login
#         self.client.login(username='admin_test', password='123')
#         res = self.client.get(reverse('dashboard'))
#         self.assertEqual(res.status_code, 200)
#         self.assertContains(res, 'Milk 500ml')

#     def test_crud_operations(self):
#         self.client.login(username='admin_test', password='123')

#         # Add Product
#         res = self.client.post(reverse('add_product'), {
#             'name': 'Ghee 500g',
#             'category': 'Ghee',
#             'quantity': 10,
#             'price': '400.00'
#         })
#         self.assertRedirects(res, reverse('dashboard'))
#         self.assertTrue(Product.objects.filter(name='Ghee 500g').exists())

#         # Edit Product
#         ghee = Product.objects.get(name='Ghee 500g')
#         res = self.client.post(reverse('edit_product', args=[ghee.id]), {
#             'name': 'Ghee 500g (Pure)',
#             'category': 'Ghee',
#             'quantity': 15,
#             'price': '420.00'
#         })
#         self.assertRedirects(res, reverse('dashboard'))
#         ghee.refresh_from_db()
#         self.assertEqual(ghee.name, 'Ghee 500g (Pure)')

#         # Delete Product
#         res = self.client.get(reverse('delete_product', args=[ghee.id]))
#         self.assertRedirects(res, reverse('dashboard'))
#         self.assertFalse(Product.objects.filter(id=ghee.id).exists())
