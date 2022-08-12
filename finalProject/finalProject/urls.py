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
from django.views.generic import TemplateView
from main.views import HomeView
from shop.views import *

from address_form.views import AddressFormView, get_address, AddresSuccessfulView

from accounts.views import profile_functionalities, basket_view

from shop.views import BreadAndBakingGoodsView, DairyProductsView, FruitAndVegetablesView, JuicesAndDrinksView, MeatView

urlpatterns = [

                path('admin/', admin.site.urls),
                path('base/', HomeView.as_view()),
                path("accounts/", include("accounts.urls"), name="accounts"),
                # path('home/', TemplateView.as_view(template_name='home.html'), name='home'), ##czy tak może zostać?
                path('home/', HomeView.as_view(template_name='home.html'), name='home'),
                path('shop/', include('shop.urls'), name='shop'),
                path('address_form/', AddressFormView.as_view()),
                path('address/', get_address),
                path('address/successful/', AddresSuccessfulView.as_view()),
                path('profile/', profile_functionalities, name='profile'),
                #path('basket/', basket_view, name='basket'),
                path('home/bread_and_baking_goods', BreadAndBakingGoodsView.as_view()),
                path('home/dairy_products', DairyProductsView.as_view()),
                path('home/fruit_and_vegetables', FruitAndVegetablesView.as_view()),
                path('home/juices_and_drinks', JuicesAndDrinksView.as_view()),
                path('home/meat', MeatView.as_view()),
]
