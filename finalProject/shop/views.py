from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Storage


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'all_products': all_products})

def all_category(request):
    all_category = Category.objects.all()
    return render(request, 'all_category.html',{'all_category': all_category})

def some_category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)

def some_product(request, id):
    product_user = Product.objects.get(pk=id)
    inscription = "<h1>" + str(product_user) + "</h1>" + \
                  "<p>" + str(product_user.price) + "</p1>" + \
                  "<p>" + str(product_user.description) + "</p1>" + \
                  "<p>" + str(product_user.measurement_unit) + "</p1>" + \
                  "<p>" + str(product_user.availability) + "</p1>"
    return HttpResponse(inscription)
