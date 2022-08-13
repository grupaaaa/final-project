from django.contrib import admin
from django.urls import path, include
from shop.views import get_categories, CategoryDetailView, get_product_detail, cart, checkout, item_increment

from django.urls import path


app_name = 'shop'
urlpatterns = [
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path("categories/", get_categories, name="category_list"),
    path('product/<int:id>', get_product_detail, name='product_detail'),
    # path('order_add/<int:id>', order_add, name='order_add'),
    path('basket/<int:id>', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path()
    # path('basket_detail/<int:pk>', checkout, name='basket_detail'),

]