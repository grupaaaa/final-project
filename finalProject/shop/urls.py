from django.contrib import admin
from django.urls import path, include
from shop.views import *




from django.urls import path





urlpatterns = [
                path('category/', CategoryListView.as_view(), name='category-list'),
                path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
                path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
                # path("products/", get_products, name="products"), #do poprawy



]