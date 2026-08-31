from django.urls import path
from . import views

# ========================================================
# URL ROUTES (Map browser URLs to python view functions)
# ========================================================
urlpatterns = [
    path('', views.dashboard, name='dashboard'),                 # Home page (http://127.0.0.1:8000/)
    path('login/', views.user_login, name='login'),              # Login page (http://127.0.0.1:8000/login/)
    path('logout/', views.user_logout, name='logout'),           # Logout (http://127.0.0.1:8000/logout/)
    path('add/', views.add_product, name='add_product'),         # Add Product (http://127.0.0.1:8000/add/)
    path('edit/<int:id>/', views.edit_product, name='edit_product'),     # Edit Product (http://127.0.0.1:8000/edit/1/)
    path('delete/<int:id>/', views.delete_product, name='delete_product'), # Delete Product (http://127.0.0.1:8000/delete/1/)
]