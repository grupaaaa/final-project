from django.contrib import admin
from django.urls import path, include
from shop.views import get_categories, CategoryDetailView, get_product_detail, order_add, order_detail

from django.urls import path




app_name = 'shop'
urlpatterns = [
    path("categories/", get_categories, name="category_list"),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:id>', get_product_detail, name='product_detail'),
    path('order_add/<int:id>', order_add, name='order_add'),
    path('basket/', order_detail, name='basket'),

]




