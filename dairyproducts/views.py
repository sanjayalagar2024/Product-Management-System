import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# ========================================================
# 1. LOGIN VIEW
# Takes username & password and checks if the user exists
# ========================================================
def user_login(request):
    # If the user is already logged in, send them directly to the dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    # When the user submits the login form (POST request)
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')

        env_user = os.getenv('ADMIN_USERNAME')
        env_pass = os.getenv('ADMIN_PASSWORD')

        # 1. Check if credentials match .env configuration
        if env_user and env_pass and username_input == env_user and password_input == env_pass:
            user, created = User.objects.get_or_create(username=env_user)
            if created or not user.check_password(env_pass):
                user.set_password(env_pass)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            login(request, user)
            return redirect('dashboard')

        # 2. Otherwise authenticate against database
        user = authenticate(request, username=username_input, password=password_input)

        if user is not None:
            login(request, user)  # Login the user
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')

    # If user just opened the login page (GET request)
    return render(request, 'login.html')


# ========================================================
# 2. LOGOUT VIEW
# Logs out the current user and redirects to login page
# ========================================================
def user_logout(request):
    logout(request)
    return redirect('login')


# ========================================================
# 3. DASHBOARD VIEW (HOME)
# Shows summary numbers and list of all products
# ========================================================
@login_required(login_url='login')
def dashboard(request):
    # 1. Fetch all products from MySQL database
    products = Product.objects.all()

    # 2. Calculate summary totals
    total_products = products.count()
    total_stock = sum(p.quantity for p in products)
    total_value = sum(p.quantity * p.price for p in products)

    # 3. Pass data to the HTML template
    context = {
        'products': products,
        'total_products': total_products,
        'total_stock': total_stock,
        'total_value': total_value,
    }
    return render(request, 'dashboard.html', context)


# ========================================================
# 4. ADD PRODUCT VIEW
# Shows form to add a new dairy product and saves it
# ========================================================
@login_required(login_url='login')
def add_product(request):
    form = ProductForm(request.POST or None)

    # If form is submitted and valid, save to database
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully!')
        return redirect('dashboard')

    return render(request, 'product_form.html', {'form': form, 'title': 'Add New Product'})


# ========================================================
# 5. EDIT PRODUCT VIEW
# Loads existing product and updates changes
# ========================================================
@login_required(login_url='login')
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)

    # If updated form is submitted and valid, save changes
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('dashboard')

    return render(request, 'product_form.html', {'form': form, 'title': 'Edit Product'})


# ========================================================
# 6. DELETE PRODUCT VIEW
# Deletes the product matching the given id
# ========================================================
@login_required(login_url='login')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('dashboard')
