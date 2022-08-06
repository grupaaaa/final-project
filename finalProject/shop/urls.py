from shop.views import *
from django.urls import path


app_name = 'shop'
urlpatterns = [
                # path('categories', CategoryListView.as_view(), name='category_list'),
                path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
                # path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
                path("categories/", get_categories, name="category_list"),
                path('product/<int:id>', get_product_detail, name='product_detail'),

]