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
                path('category/', CategoryListView.as_view(), name='category-list'),
                path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
                path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
                # path("products/", get_products, name="products"), #do poprawy

]
