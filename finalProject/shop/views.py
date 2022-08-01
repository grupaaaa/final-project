from django.shortcuts import render
from .models import Product, Category, Storage


def get_products(request):
    products = Product.objects.all()
    ctx = {'products': products}

    return render(request, 'get/products.html', context=ctx)

def get_categories(request):
    get_categories = Category.objects.all()
    ctx = {'categories': categories}

    return render(request, 'get/categories.html', contex=ctx)

def get_category(request, id: int):
    category_user = Category.objects.get(id=id)
    ctx = {"category": category}

    except Category.DoesNotExist:
    ctx = {"category_id": id}

    return render(request, 'get/category.html', contex=ctx)

def get_category(request, id: int):
    get_product = Product.objects.get(id=id)
    ctx = {"product": product}

    except Product.DoesNotExist:
    ctx = {"product_id": id}

    return render(request, 'get/product.html', contex=ctx)

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        ctx = {"products": products}

        return render(self.request, "get/products.html", context=ctx)

class ProductDetailView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            product = Product.objects.get(id=id)
            ctx = {"product": product}
        except Product.DoesNotExist:
            ctx = {"product_id": id}

        return render(self.request, "get/product.html", context=ctx)

class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        ctx = {"categories": categories}

        return render(self.request, "get/categories.html", context=ctx)

class CategoryDetailView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            category = Category.objects.get(id=id)
            ctx = {"category": category}
        except Category.DoesNotExist:
            ctx = {"category_id": id}

        return render(self.request, "get/category.html", context=ctx)




