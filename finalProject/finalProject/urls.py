"""finalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop.views import *




# from django.urls import path
from django.views.generic import TemplateView
from main.views import HomeView
from accounts.views import *


urlpatterns = [
                path('admin/', admin.site.urls),
                path('base/', HomeView.as_view()),
                path("accounts/", include("accounts.urls"), name="accounts"),
                path('h/', TemplateView.as_view(template_name='home.html'), name='home'),
                path("products/", get_products, name="products"),
                path("product/<int:id>", get_product, name="product"),
                path("categories/", get_categories, name="categories"),
                path("category/<int:id>", get_category, name="category"),
                path("cbv-posts/", ProductListView.as_view(), name="cbv_product_list"),
                path("cbv-products/<int:id>", ProductDetailView.as_view(), name="cbv_product_detail"),
                path("cbv-posts/", CategoryListView.as_view(), name="cbv_category_list"),
                path("cbv-categories/<int:id>", CategoryDetailView.as_view(), name="cbv_category_detail"),
]
