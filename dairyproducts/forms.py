from django import forms
from .models import Product

# ========================================================
# 2. PRODUCT FORM
# Automatically creates HTML input boxes for the Product model
# ========================================================
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'price']
        
        # Custom CSS styling for form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Milk 500ml'}),
            'category': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Milk, Curd, Ghee, Butter'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter stock quantity'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'placeholder': 'Enter price'}),
        }
