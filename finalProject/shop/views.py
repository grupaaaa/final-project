from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Storage

# Create your views here.
def index(request):
    allproducts = Product.objects.all()
    return HttpResponse(allproducts)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)

def product(request, id):
    product_user = Product.objects.get(pk=id)
    inscription = "<h1>" + str(product_user) + "</h1>" + \
                  "<p>" + str(product_user.price) + "</p1>" + \
                  "<p>" + str(product_user.description) + "</p1>" + \
                  "<p>" + str(product_user.measurement_unit) + "</p1>" + \
                  "<p>" + str(product_user.availability) + "</p1>"
    return HttpResponse(inscription)
