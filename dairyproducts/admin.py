from django.contrib import admin
from .models import Product

# Register Product so it can be managed inside Django Admin (/admin/)
admin.site.register(Product)
