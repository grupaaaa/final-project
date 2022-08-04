from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View


from .models import Product, Category

class ProductView(View):
    def get(self, request, *args, **kwargs):

        products = Product.objects.filter(is_active = True) #tutaj do poprawki


        context = {
            'products': products,
        }

        return render(request, 'shop/products.html', context)

class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug = slug)
        context = {
            'product': product
        }
        return render(request, 'shop/productdetail.html', context)

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.product_set.all()
        return context










