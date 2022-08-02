from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts.views import register

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', register, name='register'),
]
