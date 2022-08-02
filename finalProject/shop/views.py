from django.shortcuts import render
from django.views import View

from .models import Product, Category, Storage


def get_products(request):
    products = Product.objects.all()
    ctx = {'products': products}

    return render(request, 'get/products.html', context=ctx)

def get_categories(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}

    return render(request, 'get/categories.html', context=ctx)

def get_category(request, id: int):
    category = Category.objects.get(id=id)
    ctx = {"category": category}

    return render(request, 'get/category.html', context=ctx)

def get_product(request, id: int):
    product = Product.objects.get(id=id)
    ctx = {"product": product}

    return render(request, 'get/product.html', context=ctx)

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        ctx = {"products": products}

        return render(self.request, "get/products.html", context=ctx)

class ProductDetailView(View):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(id=id)
        ctx = {"product": product}

        return render(self.request, "get/product.html", context=ctx)

class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        ctx = {"categories": categories}

        return render(self.request, "get/categories.html", context=ctx)

class CategoryDetailView(View):
    def get(self, request, id, *args, **kwargs):
        category = Category.objects.get(id=id)
        ctx = {"category": category}

        return render(self.request, "get/category.html", context=ctx)




