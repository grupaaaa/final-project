from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View

from .models import Product, Category


class ProductDetailView(View):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    queryset = Product.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=id)

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['products'] = Product.objects.all()
        context['products'] = Product.objects.filter(category = self.get_object())
        return context











