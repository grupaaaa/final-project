from django.contrib import admin
from django.urls import path, include
from shop.views import *




from django.urls import path




app_name = 'shop'
urlpatterns = [
                path('', CategoryListView.as_view(), name='category_list'),
                path('<int:id>', CategoryDetailView.as_view(), name='category_detail'),
                path('<int:id>', ProductDetailView.as_view(), name='product_detail'),




]