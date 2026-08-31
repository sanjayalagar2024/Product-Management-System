from django.db import models

# ========================================================
# 1. PRODUCT MODEL (DATABASE TABLE)
# Each variable below creates a column in your database table.
# ========================================================
class Product(models.Model):
    name = models.CharField(max_length=100)                  # Product Name (e.g. Fresh Cow Milk)
    category = models.CharField(max_length=50, default='Milk') # Category (e.g. Milk, Curd, Ghee)
    quantity = models.IntegerField(default=0)                # Quantity in stock (e.g. 50)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Selling Price (e.g. 30.00)

    # How this product shows up as text (e.g. "Fresh Milk - ₹30.00")
    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    @property
    def total_price(self):
        return self.quantity * self.price