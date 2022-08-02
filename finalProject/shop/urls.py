from django.contrib import admin
from django.urls import path, include
from shop.views import *




from django.urls import path
from django.views.generic import TemplateView




urlpatterns = [

                path("products/", get_products, name="products"),
                path("products/<int:id>", get_product, name="product"),
                path("categories/", get_categories, name="categories"),
                path("category/<int:id>", get_category, name="category_detail"),
                path("cbv-products/", ProductListView.as_view(), name="cbv_product_list"),
                path("cbv-products/<int:id>", ProductDetailView.as_view(), name="cbv_product_detail"),
                path("cbv-categories/", CategoryListView.as_view(), name="cbv_category_list"),
                path("cbv-categories/<int:id>", CategoryDetailView.as_view(), name="cbv_category_detail"),


]