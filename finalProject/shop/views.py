from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View


from .models import Product, Category


class ProductDetailView(View):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    queryset = Product.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Product, id=id)

class CategoryListView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'shop/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        return context










