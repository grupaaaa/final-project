from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Product, Category


# class ProductDetailView(View):
#     model = Product
#     context_object_name = 'product'
#     template_name = 'shop/product_detail.html'
#     queryset = Product.objects.all()
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Product, pk=id)

def get_product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}

    return render(request, "shop/product_detail.html",context)


def get_categories(request):
    categories = Category.objects.all()
    ctx = {"categories": categories}

    return render(request, "shop/category_list.html", context=ctx)


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.get_object())
        return context
