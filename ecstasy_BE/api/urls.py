from django.urls import path
from .views import product_views, category_views

urlpatterns = [
    path('products/', product_views.product_list, name='product-list'),
    path('products/<int:pk>/', product_views.product_detail, name='product-detail'),
    # path('categories/', category_views.category_list, name='category-list'),
]
