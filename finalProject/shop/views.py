from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Storage
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def Category(request):
    all_category = Category.objects.all()
    data = {'all_category': all_category}
    return render(request, 'index.html', data)

def Categories(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)

def Product(request, id):
    product_user = Product.objects.get(pk=id)
    inscription = "<h1>" + str(product_user) + "</h1>" + \
                  "<p>" + str(product_user.price) + "</p1>" + \
                  "<p>" + str(product_user.description) + "</p1>" + \
                  "<p>" + str(product_user.measurement_unit) + "</p1>" + \
                  "<p>" + str(product_user.availability) + "</p1>"
    return HttpResponse(inscription)
