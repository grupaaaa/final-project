from django.contrib import admin
from django.urls import path, include
from shop.views import *




from django.urls import path




app_name = 'shop'
urlpatterns = [
                path('categories', CategoryListView.as_view(), name='category_list'),
                path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
                path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),






]