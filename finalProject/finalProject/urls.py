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
from shop import views




from django.urls import path
from django.views.generic import TemplateView

from main.views import HomeView


urlpatterns = [
                path('admin/', admin.site.urls),
                path('', views.all_category, name='all_products'),
                path('some_category/', views.some_category, name='some_category'),
                path('some_product/', views.some_product, name='some_product'),
                path('', views.all_category, name='all_category'),
                path('base/', HomeView.as_view()),

              ]
